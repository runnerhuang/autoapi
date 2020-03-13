# coding=UTF-8


import requests
from Common.util import decode_str, md5_s, random_8int


def Eatojoy_dataReady(eatojoy_url, eatojoy_ios_url, eatojoy_bk_token, ):
    eatojoy_pic = "/eatojoy/1b9c4b7553d94f038b3178b676b993d6.jpg"
    eatojoy_phone = str(random_8int())
    eatojoy_vendor_name = str(random_8int())

    print("创建商户：")
    url = eatojoy_url + "/admin/vendor/new_vendor"
    headers = {"eatojoy-admin-api-key": eatojoy_bk_token}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "name": "自动化测试商家" + eatojoy_vendor_name,
        "description": "自动化测试商家简介",
        "logo": eatojoy_pic,
        "tags": "z001,y001,g001",
        "spend": "40",
        "prepare_time": "0",
        "business_code": "12345678910",
        "district": "0",
        "address": "餐厅详细地址",
        "contact": "自动化",
        "lon": "114.38817",
        "lat": "22.0490721",
        "business_time": "00:00~12:00,12:00~23:59",
        "email": "zxs123456@qq.com",
        "mobile": eatojoy_phone,
        "representative": "hhhh",
        "borrow_device": 1,
        "device_info": "12312",
        "has_cash_pledge": 1,
        "cash_pledge": 1233,
        "bank_num": "123456782",
        "bank_owner": "hhh",
        "bank_type": "hhhh",
        "protocol_file": "/_docment/58625acfaefa1757a6e89b163002d4ab.jpg",
        "protocol_name": "3M以下JPG.jpg",
        "start_time": "2018-04-18",
        "end_time": "2019-05-08",
        "rate": "2",
        "settlement_cycle": "0", "vendor_type": 1,
        "remark": "1231231321",
        "status": 1
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if ret.json()["status"] == True:
        print("返回：")
        print(ret.json())
        vendor_id = ret.json()["data"]["vendor_id"]
    elif ret.json()["status"] == False:
        print("创建商户失败")
        print(ret.json())
        return False

    print("审核商户基本信息：")
    url = eatojoy_url + "/admin/vendor/base_check"
    headers = {"eatojoy-admin-api-key": eatojoy_bk_token}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "id": vendor_id,
        "result": 1,
        "remark": "自动化审核商户基本信息备注"
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
    else:
        print("审核商户基本信息失败")
        print(ret.json())
        return False

    print("审核商户合约信息：")
    url = eatojoy_url + "/admin/vendor/bank_check"
    headers = {"eatojoy-admin-api-key": eatojoy_bk_token}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "id": vendor_id,
        "result": 1,
        "remark": "自动化审核商户合约信息备注"
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
    else:
        print("审核商户银行信息失败")
        print(ret.json())
        return False

    print("审核商户合约信息：")
    url = eatojoy_url + "/admin/vendor/protocol_check"
    headers = {"eatojoy-admin-api-key": eatojoy_bk_token}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "id": vendor_id,
        "result": 1,
        "remark": "自动化审核商户合约信息备注"
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
    else:
        print("审核商户合约信息失败")
        print(ret.json())
        return False

    print("创建商品类型：")
    url = eatojoy_url + "/admin/food/add_type"
    headers = {"eatojoy-admin-api-key": eatojoy_bk_token}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "vendor_id": vendor_id,
        "num": "123",
        "sale_time": "00:00~23:59",
        "name": "自动化测试商品类型"
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
        type_id = ret.json()["data"]["type_id"]
    else:
        print("创建商品类型失败")
        print(ret.json())
        return False

    print("创建菜品：")
    url = eatojoy_url + "/admin/food/create"
    headers = {"eatojoy-admin-api-key": eatojoy_bk_token}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "vendor_id": vendor_id,
        "num": "123",
        "type": type_id,
        "name": "自动化测试菜名",
        "description": "自动化测试简介",
        "images": eatojoy_pic,
        "price": 1230,
        "has_package": 1,
        "limited_stock": 0,
        "stock": 0,
        "packages": [{
            "package_name": "12",
            "package_type": "1",
            "package_tags": [
                {
                    "tag_name": "123",
                    "tag_price": 100
                },
                {
                    "tag_name": "123",
                    "tag_price": 244
                }
            ]
        }]
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
        food_id = ret.json()["data"]["food_id"]
    else:
        print("创建菜品失败")
        print(ret.json())
        return False

    print("商家登录：")
    url = eatojoy_ios_url + "/vendor/login"
    password = md5_s(eatojoy_phone)
    print("请求地址：" + url)
    data = {
        "account": eatojoy_phone,
        "password": password,
        "uuid": "asdasd"

    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
        vendor_token = ret.json()["data"]["vendor_token"]
    else:
        print("商家登录失败")
        print(ret.json())
        return False

    print("商家开启营业：")
    url = eatojoy_ios_url + "/vendor/open"
    headers = {"Cookie": "vendor_token={0};vendor_id={1}".format(vendor_token, vendor_id)}
    print("请求头：")
    print(headers)
    print("请求地址：" + url)
    data = {
        "st": 1
    }
    print("请求参数：")
    print(decode_str(data))
    ret = requests.post(url, json=data, headers=headers)
    if str(ret.status_code).startswith("2"):
        print("返回：")
        print(ret.json())
    else:
        print("商家开启营业失败")
        print(ret.json())
        return False

    return vendor_id, vendor_token, type_id, food_id
