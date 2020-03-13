# -*- coding: utf-8 -*-
# @Date  : 2020/3/8 9:46 PM
# @Author: Runner
# @Desc  :


import requests
from Common.util import decode_str, md5_s, random_8int


def Baidu_dataReady(baidu_url, baidu_zd_url, baidu_news_url, ):
    baidu_rc = "test"
    headers = {
        'cache-control': "no-cache",
    }
    print("百度首页搜索：test")
    url = baidu_url
 #   param = {"show_env": baidu_rc}
    param = {"wd": baidu_rc}
    ret = requests.get(url, headers=headers, params=param)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        #print(ret.json())
        rc_str = "test"
    else:
        return False
    return rc_str
