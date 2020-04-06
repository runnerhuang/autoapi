import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from Config import config


def send_email(file_to_send=None, text=None, mail_to=None, attachment=True):
    """
    This function takes in recipient and will send the email to that email address with an attachment.
    :param file_to_send: the file will be send to mail_to.
    :param mail_to: the email of the person to get the text file attachment.
    :param text in the file text will be seen in email content.
    :param mail_cc the email of the cc person to get email.
    :param attachment attachment to send selection.
    """
    folder = config.folder
    project = config.ReadConfig.get_project("project").upper()
    version = config.ReadConfig.get_project("version")
    env = config.env

    if "/" in folder:
        folder = folder.replace("/", "_")
    if "\\" in folder:
        folder = folder.replace("\\", "_")
    else:
        pass
    # print(folder)
    if ";" in folder:
        folder = folder.split(";")[0].replace(folder.split(";")[0].split("_")[-1], "Multiple_Folder")
    time_str = time.strftime("%Y-%m-%d %X", time.localtime())
    # Set the server and the message details
    send_from = '%s' % config.ReadConfig.get_email("email_sender")
    # subject = "Automation TestReport FOR {0} {1}".format(folder, time_str)
    subject = "API Automation TestReport FOR {0}_{1}-{2} {3} {4}".format(project, version, env, folder, time_str)
    # Create the multi-part
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = ",".join(mail_to)  # recipient
    # msg['To'] = mail_to  # recipient
    # msg.preamble = 'MultiPart message.\n'

    # Text part of the message
    fd = open(text, 'r')
    values = ""
    p_count = 0
    f_count = 0
    e_count = 0
    not_send = 0
    value = fd.readlines()
    for each in value:
        if "P       " in each:
            p_count += 1
        elif "F       " in each:
            not_send = 1
            f_count += 1
            values += each + "<br />"
        elif "E       " in each:
            e_count += 1
            values += each + "<br />"

    a_count = p_count + f_count + e_count

    fd.close()
    if values != "":
        html = """
                    <html>
                      <head></head>
                      <body>
                            <h1>接口自动化测试报告<br /></h1>
                            Dear ALL,<br />
                            <br />
                            以下是这次接口自动化测试结果: <br />
                            执行测试用例总数（ALL） ：{0} <br />
                            通过测试用例数（PASS）  ：{1} <br />
                            <font color="#FF0000">失败测试用例数（FAIL）  ：{2}</font> <br />
                            <font color="#FF0000">错误测试用例数（ERROR） ：{3}</font> <br />
                            <br />
                            失败测试用例列表：<br />
                            {4}
                            <br />
                            所有详细的测试结果请下载附件
                            <br />
                            <br />
                            这是一封自动发送的邮件，并且不会回复任何邮件！请勿回复...<br />
                            有任何问题请联系测试部，谢谢！<br />
                            温馨提示：如果您看到的邮件是乱码，请将邮箱的查看编码格式设置为UTF-8，具体请参考不同邮箱客户端的设置。<br />
                      </body>
                    </html>
                """.format(a_count, p_count, f_count, e_count, values, file_to_send)
    else:
        html = """
            <html>
              <head></head>
              <body>
                    <h1>接口自动化测试报告<br /></h1>
                    Dear ALL,<br />
                    <br />
                    以下是这次接口自动化测试结果:<br />
                    执行测试用例总数（ALL） ：{0}<br />
                    通过测试用例数（PASS）  ：{1}<br />
                    失败测试用例数（FAIL）  ：{2}<br />
                    错误测试用例数（ERROR） ：{3}<br />
                    <br />
                    所有详细的测试结果请下载附件
                    <br />
                    <br />
                    这是一封自动发送的邮件，并且不会回复任何邮件！请勿回复...<br />
                    有任何问题请联系测试部，谢谢！<br />
                    温馨提示：如果您看到的邮件是乱码，请将邮箱的查看编码格式设置为UTF-8，具体请参考不同邮箱客户端的设置。<br />
              </body>
            </html>
        """.format(a_count, p_count, f_count, e_count, file_to_send)
    html = MIMEText(html, 'html', _charset='utf-8')
    msg.attach(html)
    if attachment:
        if isinstance(file_to_send,list):
            for SendFile in file_to_send:
                fp = open("%s" % SendFile, "rb")
                part = MIMEApplication(fp.read())
                fp.close()
                part.add_header('Content-Disposition', 'attachment', filename="%s" % SendFile)
                msg.attach(part)
        else:
            fp = open("%s" % file_to_send, "rb")
            part = MIMEApplication(fp.read())
            fp.close()
            part.add_header('Content-Disposition', 'attachment', filename="%s" % file_to_send)
            msg.attach(part)

    sp = smtplib.SMTP_SSL("smtp.qq.com", port=465)
    sp.set_debuglevel(0)
    sp.ehlo()
    sp.login(config.ReadConfig.get_email("email_sender"), config.ReadConfig.get_email("email_sender_password"))
    sp.sendmail(msg['From'], mail_to, msg.as_string())
    sp.quit()
