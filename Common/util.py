import datetime
import hashlib
import random
import string

import simplejson
import base64
import os
from random import Random
from dateutil.relativedelta import relativedelta


def get_values_by_key(input_json, key, values=list):
    key_value = None
    value = None
    if isinstance(input_json, dict):
        for json_result in input_json.values():
            if key in input_json.keys():
                key_value = input_json.get(key)
                if key_value not in values:
                    values.append(key_value)
            else:
                get_values_by_key(json_result, key, values)
    elif isinstance(input_json, list):
        for json_array in input_json:
            get_values_by_key(json_array, key, values)
    if values:
        if len(values) > 1:
            value = values
        elif len(values) == 1:
            value = values[0]
        return value
    else:
        return "Cannot find the value"


def sort_data(di, ignore="Secret Key"):
    """
    此方法为了接口文档中的Headers secret使用
    :param di: 输入参数的params
    :param ignore: 对应的secret key
    :return:
    """
    for k in di.keys():
        if ignore in di.keys():
            di.pop(ignore)
    for k in di.keys():
        if di[k] is None:
            di.pop(k)
    return "".join(["{0}={1}&".format(k, di[k]) for k in sorted(di.keys())])[:-1].encode("utf-8")


def md5_secret(in_str, serect_key):
    """
    MD5加密
    :param in_str:
    :param serect_key:
    :return:
    """
    md_str = in_str+"&secret="+serect_key
    # print md_str
    md = hashlib.md5()
    md.update(md_str.encode('utf-8'))
    md_ret = md.hexdigest().upper()
    return md_ret


def md5_s(in_str):
    """
    MD5加密
    :param in_str:
    :return:
    """
    md_str = in_str
    # print md_str
    md = hashlib.md5()
    md.update(md_str.encode('utf-8'))
    md_ret = md.hexdigest()
    return md_ret


def get_current_stamp():
    import datetime
    import time
    return str(int(time.mktime(datetime.datetime.now().timetuple())))


class OptionalException(Exception):
    pass


def get_value(property_path, data):
    count = 0
    temp = data
    for k in property_path.split("."):
        count = count + 1
        if k.endswith("?"):
            k = k[:-1]
            is_optional = True
        else:
            is_optional = False

        try:
            if k.count('1_1')==0:#临时规避data为{'1_1':{'id':1, 'name':'abc'},'2':{'id':2,'name':'cbd'}}的问题
                idx = int(k)
            else:
                idx=k
            try:
                if count == 1 and str(k).isdigit():#避免data为{'1':{'id':1, 'name':'abc'},'2':{'id':2,'name':'cbd'}}类似的问题
                    temp = temp[str(idx)]
                else:
                    temp = temp[idx]
            except IndexError as e:
                if is_optional:
                    raise OptionalException()
                else:
                    raise e
        except ValueError as e:
            try:
                if k == "len":
                    return len(temp)
                else:
                    try:
                        temp = temp[k]
                    except:
                        print('无法取到%s正确的value值，请检查格式'%property_path)
                        return False
            except KeyError as e:
                if is_optional:
                    # return None
                    raise OptionalException()
                else:
                    raise e
    return temp


def decode_str(content, encoding='utf-8'):
    # import platform
    # if "Darwin" in platform.platform():
    #     return simplejson.dumps(content, encoding=encoding, indent=4, ensure_ascii=False)
    # if "Windows" in platform.platform():
    #     return simplejson.dumps(content, encoding=encoding, indent=4, ensure_ascii=False)
    # if "Linux" in platform.platform():
    #     return simplejson.dumps(content, encoding=encoding, indent=4, ensure_ascii=False)
    # 只支持json格式
    # indent 表示缩进空格数
    # hsm20180807  ascii
    return simplejson.dumps(content, encoding=encoding, indent=4, ensure_ascii=False)

def eatojoy_date(day):
    import time
    stf_time = time.time()
    time_end = stf_time + day*3600*24
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M', x)
    return ret


def random_8int():
    import random
    x = random.randint(10000000, 99999999)
    return x

def md5_sec(in_str):
    """
    MD5加密
    :param in_str:
    :return:
    """
    # print md_str
    md = hashlib.md5()
    md.update(in_str)
    md_ret = md.hexdigest()
    return md_ret


def base64_encode(content):
    return base64.b64encode(content)


def get_device():
    value = os.popen("adb devices")
    for v in value.readlines():
        s_value = str(v).replace("\n", "").replace("\t", "")
        if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
            return s_value[:s_value.find('device')].strip()


def get_apk_path():
        """
        get test APK in prjPath
        :return:basename
        """
        ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # print ROOT_DIR
        apks = os.listdir(ROOT_DIR)
        if len(apks) > 0:
            for apk in apks:
                basename = os.path.basename(apk)
                if basename.split('.')[-1] == "apk":
                    apk_path = os.path.abspath(os.path.join(ROOT_DIR, basename))
                    return apk_path
        else:
            return None


def now():
    import time
    stf_time = time.time()
    time_end = stf_time+26
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret



def create_certificate():
    id0 = ''.join(str(i) for i in random.sample(range(0, 9), 2))
    id = ''.join(str(i) for i in random.sample(range(0, 9), 5))
    ret = '44142219'+str(id0)+'101'+str(id)
    return int(ret)

def now_time():
    import time
    ret = time.time()
    return int(ret)


def reduce_min(second):
    import time
    stf_time = time.time()
    ret = stf_time - second
    return ret


def now_hotel_dayago(second):
    import time
    stf_time = time.time()
    time_end = stf_time - second
    x = time.localtime(time_end)
    ret = time.strftime('%Y%m%d', x)
    return ret


def now_hotel_dayafter(day_num):
    s = datetime.date.today() + datetime.timedelta(days=day_num)
    s = datetime.date.strftime(s, '%Y%m%d')
    return s

def payday_ago(day_num):
    s = datetime.date.today() + datetime.timedelta(days=day_num)
    s = datetime.date.strftime(s, '%Y.%m.%d')
    return s

def now_crm_dayafter(second):
    import time
    stf_time = time.time()
    time_end = stf_time + second
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M', x)
    return ret


def now_hotel_end():
    import time
    stf_time = time.time()
    time_end = stf_time + 86400
    x = time.localtime(time_end)
    ret = time.strftime('%Y%m%d', x)
    return ret


def months_after(mon,day=None):
    import datetime
    ret = datetime.date.today() + relativedelta(months=+mon)
    if day != None:
        ret = ret + relativedelta(days=+day)
    ret = ret.strftime('%Y%m%d')
    return ret


def reduce_10s():
    import time
    stf_time = time.time()
    time_end = stf_time - 10
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def MIN_HM(second):
    import time
    stf_time = time.time()
    time_end = stf_time + second
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M', x)
    return ret


def random_str(chars, leng=20):
    str = ''
    # chars = '012345678901234567890'
    # leng = len(chars) - 1
    random = Random()
    for i in range(leng):
        str += chars[random.randint(0, leng)]
    return str


def reduce_73h():
    import time
    stf_time = time.time()
    time_end = stf_time - 73*3600
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_15h():
    import time
    stf_time = time.time()
    time_end = stf_time + 15*3600
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_15m():
    import time
    stf_time = time.time()
    time_end = stf_time + 15*60
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_20m():
    import time
    stf_time = time.time()
    time_end = stf_time + 20*60
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_21m():
    import time
    stf_time = time.time()
    time_end = stf_time + 21*60
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_5m():
    import time
    stf_time = time.time()
    time_end = stf_time + 5*60
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_10d():
    import time
    stf_time = time.time()
    time_end = stf_time + 24*3600*10 + 1200
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def increase_20d():
    import time
    stf_time = time.time()
    time_end = stf_time + 24*3600*20 + 1200
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret

def add12days():
    import time
    stf_time = time.time()
    time_end = stf_time + 1000*1000
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d', x)
    return ret


def before12days():
    import time
    stf_time = time.time()
    time_end = stf_time - 1000*1000
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d', x)
    return ret

def random_int():
    import random
    x = random.randint(10000000, 99999999)
    return x
def random_5int(*args):
    import random
    # x = random.randint(10000, 99999)
    x = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    return str(x)+'0'
def random_11int(*args):
    import random
    x = random.randint(15000000000, 16000000000)
    return x

def nextday():
    import time
    stf_time = time.time()
    time_end = stf_time + 100*100
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d', x)
    return ret


def CsvData(k):
    import csv

    # with open('/Users/shen/Desktop/work/x.csv', 'rb') as f:
    #     data = csv.reader(f)

    data = csv.reader(open('/Users/shen/Desktop/work/x.csv'))

    user_tokens =[]
    for i in data:
        user_token = []
        for j in i:
            user_token.append(j)
        user_tokens.append(user_token)

    return user_tokens[k]

def counter_int():
    import random
    x = random.randint(17100000000, 17799999999)
    return x

def counter_int2():
    import random
    x = random.randint(15100000000, 15799999999)
    return x

def counter_int3():
    import random
    x = random.randint(18100000000, 18699999999)
    return x

def nowdata(second):
    import time
    stf_time = time.time()
    time_end = stf_time+second
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d-%H-%M-%S', x)
    return ret



def CheckOutTime(second):
    import time
    stf_time = time.time()
    time_end = stf_time+second
    x = time.localtime(time_end)
    ret = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return ret


def PrepareFoodTime(second):
    import time
    x = time.localtime(int(second))
    ret = time.strftime('%H:%M', x)
    return ret

def OverTakeFoodTime():
    import time
    stf_time = time.time()
    x = stf_time - 60*60*9
    print(x)
    return int(x)


def OrderSnDB(order_id):
    order_id = int(order_id)
    if order_id%100 < 10:
        order_id = '0' + str(order_id)
        return order_id
    else:
        return order_id%100



def book_time(start, end):
    import time
    start_day = time.strftime("%Y-%m-%d" , time.localtime(time.time() + int(start)*60*60*24))
    end_day = time.strftime("%Y-%m-%d" , time.localtime(time.time() + int(end)*60*60*24))

    return '{0}~{1}'.format(start_day,end_day)




def today():
    import time
    today = time.strftime("%Y-%m-%d" , time.localtime(time.time()))

    return today

def activity_printing_time(second):
    import time
    activity_time = time.strftime("%Y-%m-%d %H:%M" , time.localtime(time.time() + second))

    return activity_time
