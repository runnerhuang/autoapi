# -*- coding: utf-8 -*-
# @Date  : 2020/3/9 2:50 PM
# @Author: Runner
# @Desc  :

import requests
from Common.util import random_11int, decode_str, random_8int
from TestData.baidu_data import preData


class BaiduPublic(object):
    def __init__(self):
        pass

    @staticmethod
    def serachtest(context, *args):
        print("start：")
        url = preData["baidu_url"] + '/post'
        headers = {"context-type": "application/json"}
        params = {'showenv': 1}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)
        preData["baidu_zd_url"] = random_11int()
        preData["eatojoy_phone"] = random_8int()
        params = {"show_env": "1"}
        data = {"employ1": {"idc": "001", "name": "runner"}, "employ2": {"idc": "002", "name": "mile"}}
        print(decode_str(data))
        ret = requests.post(url, json=data, params=params, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print(ret.json()['data'])
            print(type(ret.json()['data']))
            print(ret.json()['data']['employ2'])

            return True
        else:
            print("创建商家失败")
            print(ret.json())
