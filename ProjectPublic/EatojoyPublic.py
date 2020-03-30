# -*- coding: utf-8 -*-
# @Date  : 2018/8/6 下午4:02
# @Author: Runner
# @Desc  : Eatojoy public module
import requests
from Common.util import random_int,random_11int, decode_str, md5_s, CsvData, get_value, random_8int
import time
from concurrent.futures import ThreadPoolExecutor as pool
from Common.sql import exec_sql
from TestData.eatojoy_data import preData
from Config import config

class EatojoyPublic(object):
    def __init__(self):
        pass

    @staticmethod
    def CreateVendor(context, *args):
        print("创建商户：")
        url = preData["eatojoy_url"] + "/admin/vendor/new_vendor"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print (headers)
        print("请求地址：" + url)
        preData["eatojoy_vendor_name"] = random_11int()
        preData["eatojoy_phone"] = random_8int()
        data = {
                "name":preData["eatojoy_vendor_name"],
                "description":"自动化测试商家简介",
                "logo":preData["eatojoy_pic"],
                "tags":"z001,y001,g001",
                "spend":"40",
                "prepare_time":"0",
                "business_code":"12345678910",
                "district":"0",
                "address":"餐厅详细地址",
                "contact":"自动化",
                "lon":"114.38817",
                "lat":"22.0490721",
                "business_time":"00:00~12:00,12:00~23:59",
                "email":"zxs123456@qq.com",
                "mobile":preData["eatojoy_phone"],
                "representative":"hhhh",
                "borrow_device":1,
                "device_info":"12312",
                "has_cash_pledge":1,
                "cash_pledge":1233,
                "bank_num":"123456782",
                "bank_owner":"hhh",
                "bank_type":"hhhh",
                "protocol_file":"/_docment/be911b9f7f82a8cf5e823712504c0a94.jpg",
                "protocol_name":"3M以下JPG.jpg",
                "start_time":"2018-04-18",
                "end_time":"2019-05-08",
                "rate":"2",
                "settlement_cycle":"0",
                "remark":"1231231321",
                "status": 1,
                "vendor_type": 1
            }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if ret.json()["status"] == True:
            print("返回：")
            context.key_value.update({"vendor_id": ret.json()["data"]["vendor_id"]})
            print(context.key_value)
            return True
        elif ret.json()["status"] == False:
            print("创建商家失败")
            print(ret.json())
            # # print ret.tex
            # # print("封禁商家：")
            # url = eatojoy.preData["eatojoy_url"] + "/admin/vendor/set_block"
            # headers = {"eatojoy-admin-api-key": eatojoy.preData["eatojoy_bk_token"]}
            # # print("请求头：")
            # # print(headers)
            # # print("请求地址：" + url)
            # data = {
            #     "id": context.key_value["vendor_id"],
            #     "on": 1
            # }
            # # print("请求参数：")
            # # print(decode_str(data))
            # ret = requests.post(url, json=data, headers=headers)
            # # print("返回：")
            # # print(ret.json())
            sqlist = []
            sqlist.extend([
                {"command": "DELETE FROM e_vendor WHERE NAME = \"自动化测试商家test140\"", "db": "eatojoy"}
            ]),
            for each in sqlist:
                exec_sql(each["command"], each["db"])

        else:
            print("创建商户失败")
            print(ret.json())
            return False

    @staticmethod
    def VendorLogin(context, *args):
        url = preData["eatojoy_url"] + "/admin/vendor/detail?id={}".format(context.key_value["vendor_id"])
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        ret = requests.get(url, headers=headers)
        mobile = ret.json()["data"]["mobile"]
        print("商家登录：")
        url = preData["eatojoy_ios_url"] + "/vendor/login"

        password= md5_s(str(mobile))
        print("请求地址：" + url)
        data = {
            "account": mobile,
            "password": password,
            "uuid":"asdasd"

        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            context.key_value.update({"vendor_token": ret.json()["data"]["vendor_token"]})
            context.key_value.update({"vendor_password": password})
            print(context.key_value)
            return True
        else:
            print("商家登录失败")
            print(ret.json())
            return False

    @staticmethod
    def VendorOpen(context, *args):
        print("商家开启营业：")
        url = preData["eatojoy_ios_url"] + "/vendor/open"
        headers = {
            "Cookie": "vendor_token={0};vendor_id={1}".format(context.key_value["vendor_token"],context.key_value["vendor_id"])
        }
        print("请求地址：" + url)
        print("请求头参数：")
        print(headers)
        data = {
            "st": 1
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            return True
        else:
            print("商家开启营业失败")
            print(ret.json())
            return False




    @staticmethod
    def BaseCheck(context, *args):
        print("审核商户基本信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/base_check"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)
        data = {
                "id":context.key_value["vendor_id"],
                "result":1,
                "remark":"自动化审核商户基本信息备注"
            }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            return True
        else:
            print("审核商户基本信息失败")
            print(ret.json())
            return False

    @staticmethod
    def BankCheck(context, *args):
        print("审核商户合约信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/bank_check"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)
        data = {
            "id": context.key_value["vendor_id"],
            "result": 1,
            "remark": "自动化审核商户合约信息备注"
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            return True
        else:
            print("审核商户银行信息失败")
            print(ret.json())
            return False

    @staticmethod
    def ProtocolCheck(context, *args):
        print("审核商户合约信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/protocol_check"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print (headers)
        print("请求地址：" + url)
        data = {
            "id": context.key_value["vendor_id"],
            "result": 1,
            "remark": "自动化审核商户合约信息备注"
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            return True
        else:
            print("审核商户合约信息失败")
            print(ret.json())
            return False

    @staticmethod
    def AddType(context, type=''):
        print("创建商品类型：")
        url = preData["eatojoy_url"] + "/admin/food/add_type"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print (headers)
        print("请求地址：" + url)
        if type == 'book':
            data = {
                "vendor_id": context.key_value["vendor_id"],
                "num": "123",
                "name": "自动化测试商品类型"
            }
        else:
            data = {
                "vendor_id": context.key_value["vendor_id"],
                "num": "123",
                "sale_time": "00:00~23:59",
                "name": "自动化测试商品类型"
            }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            context.key_value.update({"type_id": ret.json()["data"]["type_id"]})
            print(context.key_value)
            return True
        else:
            print("创建商品类型失败")
            print(ret.json())
            return False



    @staticmethod
    def CreateFood(context, *args):
        print("创建菜品：")
        url = preData["eatojoy_url"] + "/admin/food/create"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)
        food_name = "自动化测试菜名"
        data = {
                  "vendor_id": context.key_value["vendor_id"],
                  "num": "123",
                  "type": context.key_value["type_id"],
                  "name": food_name,
                  "description": "自动化测试简介",
                  "images": preData["eatojoy_pic"],
                  "price": 123,
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
            print (ret.json())
            context.key_value.update({"food_id": ret.json()["data"]["food_id"]})
            context.key_value.update({"food_name": food_name})
            print(context.key_value)
            return True
        else:
            print("创建菜品失败")
            print(ret.json())
            return False


    @staticmethod
    def BlockVendor(context, *args):
            print("封禁商家：")
            url = preData["eatojoy_url"] + "/admin/vendor/set_block"
            headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "id": context.key_value["vendor_id"],
                "on": 1
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            if str(ret.status_code).startswith("2"):
                print("返回：")
                print (ret.json())
                return True
            else:
                print("封禁商家失败")
                print(ret.json())
                return False

    @staticmethod
    def DeleteFodd(context, *args):
        print("删除菜品：")
        url = preData["eatojoy_url"] + "admin/food/delete"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)
        data = {
            "ids": context.key_value["food_id"],
            "vendor_id": context.key_value["vendor_id"]
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            return True
        else:
            print("删除菜品失败")
            print(ret.json())
            return False

    @staticmethod
    def UserIndex(context, *args):
        print("查看用户信息：")
        url = preData["eatojoy_url"] + "/user/user/index"
        headers = {"token": CsvData(preData["eatojoy_num"])[0]}
        preData["eatojoy_num"] = preData["eatojoy_num"] + 1
        print("请求头：")
        print(headers)
        print("请求地址：" + url)
        data = {
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.get(url, json=data, headers=headers)
        if str(ret.status_code).startswith("2"):
            print("返回：")
            print (ret.json())
            return True
        else:
            print("查看用户信息失败")
            print(ret.json())
            return False

    @staticmethod
    def CouponCheckout(context, *args):
        if ('ALL' in config.folder):
            url = preData["eatojoy_url"] + "/user/vendor/detail"
            headers = {"token": preData["eatojoy_user_token"]}
            try:
                vendor_id = context.key_value["vendor_id"]
                food_id = context.key_value["food_id"]
            except:
                vendor_id = preData["vendor_id"]
                food_id = preData["food_id"]
            data = {
                "id": vendor_id
            }
            ret = requests.get(url, json=data, headers=headers)
            print(ret.json())
            order_product_counts = ret.json()["data"]["total_amount"]
            print("下使用了优惠券的订单：")
            url = preData["eatojoy_url"] + "/user/order/checkout"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            stf_time = time.time()
            time_end = stf_time + 6
            x = time.localtime(time_end)
            take_food_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            if context.key_value["coupon_type"] == '1':
                order_grand_total = float(context.key_value["order_grand_total"])-float(context.key_value["coupon_type_value"])
                coupons_fee = context.key_value["coupon_type_value"]
            else:
                coupons_fee = (1.0-float(context.key_value["coupon_type_value"])/10.0)*float(context.key_value["order_grand_total"])
                order_grand_total = float(context.key_value["coupon_type_value"])/10.0*float(context.key_value["order_grand_total"])


            data = {
                "product_id": food_id,
                "merchants_id": vendor_id,
                "order_product_counts": order_product_counts,
                "order_grand_total": order_grand_total,
                "take_food_time": take_food_time,
                "package_fee": 10,
                "coupons_fee": coupons_fee,
                "coupon_user_code": context.key_value["coupon_user_code"]
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            if str(ret.status_code).startswith("2"):
                print("返回：")
                print (ret.json())
                context.key_value.update({"order_id": ret.json()["data"]})
                return True
            else:
                print("下使用了优惠券的订单失败")
                print(ret.json())
                return False
        else:
            print("下使用了优惠券的订单：")
            url = preData["eatojoy_url"] + "/user/order/checkout"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            stf_time = time.time()
            time_end = stf_time + 6
            x = time.localtime(time_end)
            take_food_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            if context.key_value["coupon_type"] == '1':
                order_grand_total = float(context.key_value["order_grand_total"]) - int(
                    float(context.key_value["coupon_type_value"]))
                coupons_fee = context.key_value["coupon_type_value"]
            else:
                coupons_fee = (1.0 - float(context.key_value["coupon_type_value"]) / 10.0) * float(
                    context.key_value["order_grand_total"])
                order_grand_total = float(context.key_value["coupon_type_value"]) / 10.0 * float(
                    context.key_value["order_grand_total"])

            data = {
                "product_id": context.key_value["food_id"],
                "merchants_id": context.key_value["vendor_id"],
                "order_product_counts": context.key_value["product_num"],
                "order_grand_total": order_grand_total,
                "take_food_time": take_food_time,
                "package_fee": 10,
                "coupons_fee": coupons_fee,
                "coupon_user_code": context.key_value["coupon_user_code"]
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            if str(ret.status_code).startswith("2"):
                print("返回：")
                print(ret.json())
                if "\"status\":false" in ret.json():
                    return False
                context.key_value.update({"order_id": ret.json()["data"]})
                return True
            else:
                print("下使用了优惠券的订单失败")
                print(ret.json())
                return False



    @staticmethod
    def QuickCheckout(context, *args):
        if('ALL' in config.folder):
            url = preData["eatojoy_url"] + "/user/vendor/detail"
            headers = {"token": preData["eatojoy_user_token"]}
            try:
                vendor_id = context.key_value["vendor_id"]
                food_id = context.key_value["food_id"]
            except:
                vendor_id = preData["vendor_id"]
                food_id = preData["food_id"]
            data = {
                "id":vendor_id
            }
            ret = requests.get(url, json=data, headers=headers)
            order_product_counts = ret.json()["data"]["total_amount"]
            print("下立刻取餐的订单：")
            url = preData["eatojoy_url"] + "/user/order/checkout"
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            stf_time = time.time()
            time_end = stf_time+6
            x = time.localtime(time_end)
            take_food_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            data = {
                "product_id": food_id,
                "merchants_id": vendor_id,
                "order_product_counts": order_product_counts,
                "order_grand_total": context.key_value["order_grand_total"],
                "take_food_time": take_food_time,
                "package_fee": 10,
                "coupons_fee": 0,
                "order_msg":"订单描述"
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print("返回：")
            print(ret.json())
            if str(ret.status_code).startswith("2"):
                context.key_value.update({"order_id": ret.json()["data"]})
                call_back = "https://eatojoy-app.hktester.com/orderDetail?backType=02&orderId=" + context.key_value["order_id"]

                print("提交支付申请：")
                url = preData["eatojoy_url"] + "/user/payment/web"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)

                data = {
                    "order_id": context.key_value["order_id"],
                    "call_back": call_back
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)
                print("返回：")
                print(ret.json())
                if str(ret.status_code).startswith("2"):

                    transactionId = str(ret.json()['data']['transactionId'])

                    print("支付：")
                    url = "https://eatojoy-api.hktester.com/api/payment/notification/wezero"
                    headers = {"token": preData["eatojoy_user_token"],"is-test":"yes"}
                    print("请求头：")
                    print(headers)
                    print("请求地址：" + url)

                    data = {
                        "tranId": transactionId,
                        "issueAt": str(int(time.time())),
                        "merchantTranId": context.key_value["order_id"],
                        "amount": context.key_value["order_grand_total"],
                        "success": True,
                        "from": "hk01"

                    }
                    print("请求参数：")
                    print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    print("返回：")
                    print(ret.json())
                    if str(ret.status_code).startswith("2"):
                        print("支付成功")
                        return True
                    else:
                        print("支付失败")
                        return False


                else:
                    print("提交支付失败")
                    return False
            else:
                print("下立刻取餐的订单失败")
                return False
        else:
            print("下立刻取餐的订单：")
            url = preData["eatojoy_url"] + "/user/order/checkout"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            stf_time = time.time()
            time_end = stf_time+6
            x = time.localtime(time_end)
            take_food_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            data = {
                "product_id": context.key_value["food_id"],
                "merchants_id": context.key_value["vendor_id"],
                "order_product_counts": context.key_value["product_num"],
                "order_grand_total": context.key_value["order_grand_total"],
                "take_food_time": take_food_time,
                "package_fee": 10,
                "coupons_fee": 0
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print("返回：")
            print(ret.json())
            if str(ret.status_code).startswith("2"):
                context.key_value.update({"order_id": ret.json()["data"]})
                call_back = "https://eatojoy-app.hktester.com/orderDetail?backType=02&orderId=" + context.key_value[
                    "order_id"]

                print("提交支付申请：")
                url = preData["eatojoy_url"] + "/user/payment/web"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)

                data = {
                    "order_id": context.key_value["order_id"],
                    "call_back": call_back
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)
                print("返回：")
                print(ret.json())
                if str(ret.status_code).startswith("2"):

                    transactionId = str(ret.json()['data']['transactionId'])

                    print("支付：")
                    url = "https://eatojoy-api.hktester.com/api/payment/notification/wezero"
                    headers = {"token": preData["eatojoy_user_token"], "is-test": "yes"}
                    print("请求头：")
                    print(headers)
                    print("请求地址：" + url)

                    data = {
                        "tranId": transactionId,
                        "issueAt": str(int(time.time())),
                        "merchantTranId": context.key_value["order_id"],
                        "amount": context.key_value["order_grand_total"],
                        "success": True,
                        "from": "hk01"

                    }
                    print("请求参数：")
                    print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    print("返回：")
                    print(ret.json())
                    if str(ret.status_code).startswith("2"):
                        print("支付成功")
                        return True
                    else:
                        print("支付失败")
                        return False


                else:
                    print("提交支付失败")
                    return False
            else:
                print("下立刻取餐的订单失败")
                return False


    @staticmethod
    def Android_QuickCheckout(context, *args):
        if('ALL' in config.folder):
            url = preData["eatojoy_android_url"] + "/user/vendor/detail"
            headers = {"token": preData["eatojoy_user_token"]}
            data = {
                "id":preData["vendor_id"]
            }
            ret = requests.get(url, json=data, headers=headers)
            order_product_counts = ret.json()["data"]["total_amount"]
            print("下立刻取餐的订单：")
            url = preData["eatojoy_android_url"] + "/user/order/checkout"
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            stf_time = time.time()
            time_end = stf_time+6
            x = time.localtime(time_end)
            take_food_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            data = {
                "product_id": preData["food_id"],
                "merchants_id": preData["vendor_id"],
                "order_product_counts": order_product_counts,
                "order_grand_total": context.key_value["order_grand_total"],
                "take_food_time": take_food_time,
                "package_fee": 10,
                "coupons_fee": 0,
                "order_msg":"订单描述"
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print("返回：")
            print(ret.json())
            if str(ret.status_code).startswith("2"):
                context.key_value.update({"order_id": ret.json()["data"]})
                call_back = "https://eatojoy-app.hktester.com/orderDetail?backType=02&orderId=" + context.key_value[
                    "order_id"]

                print("提交支付申请：")
                url = preData["eatojoy_url"] + "/user/payment/web"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)

                data = {
                    "order_id": context.key_value["order_id"],
                    "call_back": call_back
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)
                print("返回：")
                print(ret.json())
                if str(ret.status_code).startswith("2"):

                    transactionId = str(ret.json()['data']['transactionId'])

                    print("支付：")
                    url = "https://eatojoy-api.hktester.com/api/payment/notification/wezero"
                    headers = {"token": preData["eatojoy_user_token"], "is-test": "yes"}
                    print("请求头：")
                    print(headers)
                    print("请求地址：" + url)

                    data = {
                        "tranId": transactionId,
                        "issueAt": str(int(time.time())),
                        "merchantTranId": context.key_value["order_id"],
                        "amount": context.key_value["order_grand_total"],
                        "success": True,
                        "from": "hk01"

                    }
                    print("请求参数：")
                    print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    print("返回：")
                    print(ret.json())
                    if str(ret.status_code).startswith("2"):
                        print("支付成功")
                        return True
                    else:
                        print("支付失败")
                        return False


                else:
                    print("提交支付失败")
                    return False
            else:
                print("下立刻取餐的订单失败")
                return False
        else:
            print("下立刻取餐的订单：")
            url = preData["eatojoy_android_url"] + "/user/order/checkout"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            stf_time = time.time()
            time_end = stf_time+6
            x = time.localtime(time_end)
            take_food_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            data = {
                "product_id": context.key_value["food_id"],
                "merchants_id": context.key_value["vendor_id"],
                "order_product_counts": context.key_value["product_num"],
                "order_grand_total": context.key_value["order_grand_total"],
                "take_food_time": take_food_time,
                "package_fee": 10,
                "coupons_fee": 0
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print("返回：")
            print(ret.json())
            if str(ret.status_code).startswith("2"):
                context.key_value.update({"order_id": ret.json()["data"]})
                call_back = "https://eatojoy-app.hktester.com/orderDetail?backType=02&orderId=" + context.key_value[
                    "order_id"]

                print("提交支付申请：")
                url = preData["eatojoy_url"] + "/user/payment/web"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)

                data = {
                    "order_id": context.key_value["order_id"],
                    "call_back": call_back
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)
                print("返回：")
                print(ret.json())
                if str(ret.status_code).startswith("2"):

                    transactionId = str(ret.json()['data']['transactionId'])

                    print("支付：")
                    url = "https://eatojoy-api.hktester.com/api/payment/notification/wezero"
                    headers = {"token": preData["eatojoy_user_token"], "is-test": "yes"}
                    print("请求头：")
                    print(headers)
                    print("请求地址：" + url)

                    data = {
                        "tranId": transactionId,
                        "issueAt": str(int(time.time())),
                        "merchantTranId": context.key_value["order_id"],
                        "amount": context.key_value["order_grand_total"],
                        "success": True,
                        "from": "hk01"

                    }
                    print("请求参数：")
                    print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    print("返回：")
                    print(ret.json())
                    if str(ret.status_code).startswith("2"):
                        print("支付成功")
                        return True
                    else:
                        print("支付失败")
                        return False


                else:
                    print("提交支付失败")
                    return False
            else:
                print("下立刻取餐的订单失败")
                return False






    @staticmethod
    def LotCartAdd(context, *args):
        for i in range(1,7):
            print("加入购物车：")
            url = preData["eatojoy_url"] + "/user/cart/add"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "product_id": "1",
                "vendor_id": "2",
                "product_num": 1,"product_msg": "产品备注"
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)

            print("返回：")
            print(ret.json())
            print("购物车列表：")
            url = preData["eatojoy_url"] + "/user/cart/list"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "vendor_id": "2",
                "lon": "114.082846",
                "lat": "22.4167417"
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.get(url, json=data, headers=headers)
            print(ret.json())
            id = ret.json()["data"]["product_list"][0]["id"]
            product_num = ret.json()["data"]["product_list"][0]["product_num"]
            order_grand_total = ret.json()["data"]["price_total"]

            print("返回：")
            print(ret.json())


            print("下单：")
            url = preData["eatojoy_url"] + "/user/order/checkout"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "product_id": id,
			    "merchants_id": "2",
			    "order_product_counts": product_num,
			    "order_grand_total": order_grand_total,
                "take_food_time": preData["eatojoy_take_food_time"],
			    "package_fee":10,
                "coupons_fee":0
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print(ret.json())

            preData["eatojoy_order_id"].append(get_value("data", ret.json()))

            if i == 6:
                print(preData["eatojoy_order_id"])
                return True

    @staticmethod
    def LotCartAdd(context, *args):
            for i in range(1, 6):
                print("加入购物车：")
                url = preData["eatojoy_url"] + "/user/cart/add"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)
                data = {
                    "product_id": "1",
                    "vendor_id": "2",
                    "product_num": 1,"product_msg": "产品备注"
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)

                print("返回：")
                print(ret.json())
                print("购物车列表：")
                url = preData["eatojoy_url"] + "/user/cart/list"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)
                data = {
                    "vendor_id": "2",
                    "lon": "114.082846",
                    "lat": "22.4167417"
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.get(url, json=data, headers=headers)
                print(ret.json())
                id = ret.json()["data"]["product_list"][0]["id"]
                product_num = ret.json()["data"]["product_list"][0]["product_num"]
                order_grand_total = ret.json()["data"]["price_total"]

                print("返回：")
                print(ret.json())

                print("下单：")
                url = preData["eatojoy_url"] + "/user/order/checkout"
                headers = {"token": preData["eatojoy_user_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)
                data = {
                    "product_id": id,
                    "merchants_id": "2",
                    "order_product_counts": product_num,
                    "order_grand_total": order_grand_total,
                    "take_food_time": preData["eatojoy_take_food_time"],
                    "package_fee": 10,
                    "coupons_fee": 0
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)
                print(ret.json())

                preData["eatojoy_order_id"].append(get_value("data", ret.json()))

                if i == 5:
                    print(preData["eatojoy_order_id"])
                    return True

    @staticmethod#需要多个token
    def ConcurrencyCartAdd(context, *args):
        def checkout():
            print("加入购物车：")
            url = preData["eatojoy_url"] + "/user/cart/add"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "product_id": "1",
                "vendor_id": "2",
                "product_num": 1,"product_msg": "产品备注"
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)

            print("返回：")
            print(ret.json())
            print("购物车列表：")
            url = preData["eatojoy_url"] + "/user/cart/list"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "vendor_id": "2",
                "lon": "114.082846",
                "lat": "22.4167417"
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.get(url, json=data, headers=headers)
            print(ret.json())
            id = ret.json()["data"]["product_list"][0]["id"]
            product_num = ret.json()["data"]["product_list"][0]["product_num"]
            order_grand_total = ret.json()["data"]["price_total"]

            print("返回：")
            print(ret.json())

            print("下单：")
            url = preData["eatojoy_url"] + "/user/order/checkout"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "product_id": id,
                "merchants_id": "2",
                "order_product_counts": product_num,
                "order_grand_total": order_grand_total,
                "take_food_time": preData["eatojoy_take_food_time"],
                "package_fee": 10,
                "coupons_fee": 0
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print(ret.json())

            preData["eatojoy_order_id"].append(get_value("data", ret.json()))

        try:
            time1 = time.clock()
            with pool(max_workers=100) as executor:
                future_tasks = [executor.submit(checkout) for i in range(1,100)]

            time2 = time.clock()
            times = time2 - time1
            print(times)
            print(preData["eatojoy_order_id"])
            return True

        except Exception as e:
            print(e)





    @staticmethod
    def ConcurrencyPay(context, *args):
        def pay(order_id):
            print("支付：")
            url = preData["eatojoy_url"] + "/user/payment/pay"
            headers = {"token": preData["eatojoy_user_token"]}
            print("请求头：")
            print(headers)
            print("请求地址：" + url)
            data = {
                "order_id": order_id,
                "source_id": preData["eatojoy_source_id"]
            }
            print("请求参数：")
            print(decode_str(data))
            ret = requests.post(url, json=data, headers=headers)
            print("返回：")
            timeX = time.clock()
            print(timeX)
            print(ret.json())

        try:
            time1 = time.clock()
            thread_count = len(preData["eatojoy_order_id"])
            with pool(max_workers=100) as executor:
                future_tasks = [executor.submit(pay, order_id) for order_id in preData["eatojoy_order_id"]]


                # for order_id in eatojoy.preData["eatojoy_order_id"]:
                #     executor.submit(pay(order_id))
            time2 = time.clock()
            times = time2 - time1
            print(times / thread_count)
            return True


        # try:
        #     time1 = time.clock()
        #     thread_count = len(eatojoy.preData["eatojoy_order_id"])
        #     for order_id in eatojoy.preData["eatojoy_order_id"]:
        #         threading.Thread(target = pay(order_id))
        #     time2 = time.clock()
        #     times = time2 - time1
        #     print(times / thread_count)
        #     return True

        except Exception as e:
            print(e)

    @staticmethod
    def CreatePreVendor(context, *args):
        print("创建商户基本信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/new_vendor"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print (headers)
        print("请求地址：" + url)
        preData["eatojoy_vendor_name"] = random_11int()
        preData["eatojoy_phone"] = random_8int()
        data = {
                "name":preData["eatojoy_vendor_name"],
                "description":"预售店01",
                "logo":preData["eatojoy_pic"],
                "tags":"z001,y001,g001",
                "spend": "40",
                "vendor_type": 2,
                "book_time_type": 2,
                "book_time_value": "2",
                "prepare_time": 0,
                "expiry_date_type": "2",
                "expiry_date_value": 1,
                "stocking_time": 0,
                "stocking_time_type": 2,
                "business_code": "12345678910",
                "district": "0",
                "address":"餐厅详细地址",
                "contact":"自动化",
                "lon":"114.38817",
                "lat":"22.0490721",
                "business_time":"00:00~12:00,12:50~23:59",
                "email":"zxs123456@qq.com",
                "mobile":preData["eatojoy_phone"],
                "representative":"hhhh",
                "borrow_device":1,
                "device_info":"12312",
                "has_cash_pledge":1,
                "cash_pledge":1233,
                "status": 0
            }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if ret.json()["status"] == True:
            print("返回：")
            print (ret.json())
            eatojoy_vendor_id=ret.json()["data"]["vendor_id"]
            context.key_value.update({"vendor_id": ret.json()["data"]["vendor_id"]})
            print(eatojoy_vendor_id)
        else:
            print (ret.json())
            print("创建商家基本信息失败")

        print("添加商家财务信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/edit_vendor"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print (headers)
        print("请求地址：" + url)
        data = {
                "bank_num":"123456782",
                "bank_owner":"hhh",
                "bank_type":"hhhh",
                "status": 0,
                "vendor_id":eatojoy_vendor_id
            }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url,json = data, headers=headers)
        if ret.json()["status"] == True:
            print("返回")
            print (ret.json())
            print ("创建商家财务信息成功")

        else:
            print(ret.json())
            print("创建商家银信息失败")

        print("添加商家合约信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/edit_vendor"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)

        data = {
            "protocol_file": "/_docment/58625acfaefa1757a6e89b163002d4ab.jpg",
            "protocol_name": "3M以下JPG.jpg",
            "start_time": "2018-04-18",
            "end_time": "2019-05-08",
            "rate": "2",
            "settlement_cycle": "0",
            "remark": "1231231321",
            "status": 1,
            "vendor_id":eatojoy_vendor_id
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if ret.json()["status"] == True:
            print("返回")
            print(ret.json())
            print("创建商家合约信息成功")

        else:
            print(ret.json())
            print("创建商家合约信息失败")

        print("审核商家基础信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/base_check"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)

        data = {
            "id": eatojoy_vendor_id,
            "result": 1,
            "remark": "自动化商家基础信息审核备注"
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if ret.json()["status"] == True:
            print("返回")
            print(ret.json())
            print("商家基础信息审核通过")

        else:
            print(ret.json())
            print("商家基础信息审核失败")

        print("审核商家财务信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/bank_check"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)

        data = {
            "id": eatojoy_vendor_id,
            "result": 1,
            "remark": "自动化商家财务信息审核备注"
        }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)
        if ret.json()["status"] == True:
            print("返回")
            print(ret.json())
            print("商家财务信息审核通过")

        else:
            print(ret.json())
            print("商家财务信息审核失败")

        print("审核合约财务信息：")
        url = preData["eatojoy_url"] + "/admin/vendor/protocol_check"
        headers = {"eatojoy-admin-api-key": preData["eatojoy_bk_token"]}
        print("请求头：")
        print(headers)
        print("请求地址：" + url)

        data = {
                "id": eatojoy_vendor_id,
                "result": 1,
                "remark": "自动化商家合约信息审核备注"
            }
        print("请求参数：")
        print(decode_str(data))
        ret = requests.post(url, json=data, headers=headers)

        if ret.json()["status"] == True:
            print("返回")
            print(ret.json())
            print("商家合约信息审核通过")
            return True


        else:
            print(ret.json())
            print("商家合约信息审核失败")

