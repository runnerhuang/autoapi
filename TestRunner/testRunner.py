import codecs
from selenium import webdriver
import os
from unittest import TestSuite
from TestRunner.HTMLTestRunner import HTMLTestRunner as Tr
from Common.sendEmail import send_email
from Config import config
from TestRunner.testReport import TestReport
import platform


class TestRunner(object):

    @staticmethod
    def test_suite():

        t_suite = TestSuite()
        # import importlib  closed 20180802
        # m = importlib.import_module("ApiExecutor.API", 'API')
        from Common import API
        if config.runlist > 0:  # add 202004
            t_suite.addTest(API.suite_file())
        else:
            t_suite.addTest(API.suite())
        return t_suite

    @staticmethod
    def run():
        email = int(config.email)  # int(os.environ.get('email', 0))
        global report_file, text, runner, fp, report_title
        report_file = TestReport.generate_report("Report")
        fp = codecs.open(report_file, 'wb+')
        report_title = "Report" + "_" + config.ReadConfig.get_project("project").upper() + "_" \
                       + config.ReadConfig.get_project("version") + "-" + config.env
        runner = Tr(stream=fp, verbosity=2, title=report_title, description=report_file)
        runner.run(TestRunner.test_suite())
        fp.close()

        text = TestReport.get_log_path()

        if email != 0:
            mail_rec = ([config.ReadConfig.get_email("email_receiver")][0]).split(",")
            send_email(report_file, text, mail_rec, True)

        if platform.system() == "Windows":
            os.popen("del {0}".format(text))
        else:
            os.popen("rm {0}".format(text))

        try:
            driver = webdriver.Firefox()
        except BaseException:
            print('当前环境浏览器不支持')
        else:
            report_url = report_file.replace(os.path.dirname(os.getcwd()), 'http://localhost:63342')
            driver.get(report_url)
