# -*- coding: utf-8 -*-
# @Date  : 2018/8/2 下午6:09
# @Author: Runner
# @Desc  : eatojoy predata

from Common.util import reduce_10s, increase_15m, random_int, increase_21m, md5_s, random_8int, eatojoy_date
from Config import config


preData = {
    "eatojoy_url": config.ReadConfig.get_url('eatojoy_url'),
    "eatojoy_ios_url": config.ReadConfig.get_url('eatojoy_ios_url'),
    "eatojoy_android_url": config.ReadConfig.get_url('eatojoy_android_url'),
    "eatojoy_source_id": config.ReadConfig.get_url('eatojoy_source_id'),
    "eatojoy_user_token": config.ReadConfig.get_url('eatojoy_user_token'),
    "eatojoy_bk_token": config.ReadConfig.get_url('eatojoy_bk_token'),
    "eatojoy_pic": "/eatojoy/1b9c4b7553d94f038b3178b676b993d6.jpg",
    "eatojoy_take_food_time": increase_21m(),
    "eatojoy_pay_time_start": reduce_10s(),
    "eatojoy_pay_time_end": increase_15m(),
    "eatojoy_order_id": [],
    "eatojoy_vendor_id": 1111,
    "eatojoy_phone": random_int(),
    "eatojoy_vendor_name": "自动化测试" + str(random_int()),
    "eatojoy_num": 1,
    "eatojoy_Random_User": random_int(),
    "eatojoy_bind":md5_s(str(random_8int())),
    "eatojoy_password":md5_s("12345678"),
    "eatojoy_cc_password":"8d7ba5939bc2a3ecdc86c22477dc88db",
    "eatojoy_today":eatojoy_date(0),
    "eatojoy_1day":eatojoy_date(1),
    "eatojoy_2day":eatojoy_date(2),
    "eatojoy_1000day":eatojoy_date(2000),
    "eatojoy_10001day":eatojoy_date(1001),

    }



if config.dataready == '1':
    from TestData.eatojoy_dataReady import Eatojoy_dataReady
    data_Ready = []
    data_Ready = Eatojoy_dataReady(preData["eatojoy_url"], preData["eatojoy_ios_url"], preData["eatojoy_bk_token"])
    preData.update({
        "vendor_id": data_Ready[0],
        "vendor_token": data_Ready[1],
        "type_id": data_Ready[2],
        "food_id": data_Ready[3]
    })

    if "WEB//ALL" in config.folder:
        preData.update({
            "eatojoy_user_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE1MzYxMzAxNTQsImV4cCI6MTU0NDk5NDE1NCwiYWNjb3VudElkIjoiMTAwMDQ1MCJ9.G0kMhn0sAqkJ_WSVZ9KL7tD6x6Hc3Brf6u1yxYn-RswK_8lNItRAENSIgmSELfHvE2-ZohxPJlrFK7g46gG87ussU3GKeMqujI5fks3Od6SpPMc3f6sEplXGIEly9bMuHaE2VISzZxFhFkn0ls6USgb8qCIjWch6H3Ihy5-YfU0ZGAczxw63GQ3aq08nx5ntvb_TxU8k8wxQUy8jDT-oWyaCNIb_NBOSAYngsRbtufOn47YfMz-tuK1h-TrA6zSWt06cug0k0WotpXfcnQQ_KaLcSb0FdJOICn__0f43Wh2YqUGLq57uZ_X6TQkLTnjwHUegSjeiLuyGkoK1cMdFVQ",
            "eatojoy_source_id": "card_1CzOKsFOfYhptLUabOZFRjW3"
        })