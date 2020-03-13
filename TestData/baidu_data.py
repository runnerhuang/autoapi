# -*- coding: utf-8 -*-
# @Date  : 2020/3/8 9:22 PM
# @Author: Runner
# @Desc  :


from Common.util import reduce_10s, increase_15m, random_int, increase_21m, md5_s, random_8int
from Config import config

preData = {
    "zy_url": config.ReadConfig.get_url('zy_url'),
    "baidu_url": config.ReadConfig.get_url('baidu_url'),
    "baidu_zd_url": config.ReadConfig.get_url('baidu_zd_url'),
    "baidu_news_url": config.ReadConfig.get_url('baidu_news_url'),
    "baidu_reci": config.ReadConfig.get_url('baidu_reci'),
    "baidu_nb": "自动化测试" + str(random_int()),
    "baidu_num": 1,
    "baidu_Random_User": random_int(),
    "baidu_bind": md5_s(str(random_8int())),
}

if config.dataready == '1':
    from TestData.baidu_dataReady import Baidu_dataReady

    data_Ready = []
    data_Ready = Baidu_dataReady(preData["eatojoy_url"], preData["eatojoy_ios_url"], preData["eatojoy_bk_token"])
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
