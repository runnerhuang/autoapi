# -*- coding: utf-8 -*-
import requests
from Common.util import decode_str
from Common.sql import exec_sql
import traceback
from Config import config
import re
folder = config.folder


def tear_down(context, *args):
    sqlist = []
    try:

        if "EATOJOY" in folder:
            # import the project data before use
            from TestData import eatojoy_data

            if "banner_id" in context.key_value.keys():
                sqlist = []
                banner_id = context.key_value["banner_id"]
                sqlist.extend([
                    {"command": "delete from e_banner where id={0}".format(int(banner_id)), "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')

            if "printing_acticity_id" in context.key_value.keys():
                sqlist = []
                id = context.key_value["e_activity_printing"]
                sqlist.extend([
                    {"command": "delete from e_activity_printing where id={0}".format(int(e_activity_printing)), "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')


            if "feedback_id" in context.key_value.keys():
                sqlist = []
                feedback_id = context.key_value["feedback_id"]
                sqlist.extend([
                    {"command": "delete from e_feedback where id={0}".format(int(feedback_id)), "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')

            if "article_id" in context.key_value.keys():
                sqlist = []
                article_id = context.key_value["article_id"]
                sqlist.extend([
                    {"command": "delete from e_article where id={0}".format(int(article_id)), "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')

            # if "type_id" in context.key_value.keys():
            #     sqlist = []
            #     print(context.key_value.keys())
            #     print(context.key_value)
            #     try:
            #         vendor_id = context.key_value["vendor_id"]
            #     except:
            #         vendor_id = eatojoy_data.preData["vendor_id"]
            #     sqlist.extend([
            #         {"command": "delete from e_food_type where vendor_id={0}".format(int(vendor_id)), "db": "eatojoy"}
            #     ]),
            #     for each in sqlist:
            #         exec_sql(each["command"], each["db"])
            #         print(str(each) + '执行TearDown成功！')
            #
            # if "food_id" in context.key_value.keys():
            #     sqlist = []
            #     # print("删除菜品：")
            #     url = eatojoy_data.preData["eatojoy_url"] + "/admin/food/delete"
            #     headers = {"eatojoy-admin-api-key": eatojoy_data.preData["eatojoy_bk_token"]}
            #     # print("请求头：")
            #     # print(headers)
            #     # print("请求地址：" + url)
            #     try:
            #         vendor_id = context.key_value["vendor_id"]
            #     except:
            #         vendor_id = eatojoy_data.preData["vendor_id"]
            #     data = {
            #         "ids": context.key_value["food_id"],
            #         "vendor_id": vendor_id
            #     }
            #     # print("请求参数：")
            #     # print(decode_str(data))
            #     ret = requests.post(url, json=data, headers=headers)
            #     if str(ret.status_code).startswith("2"):
            #         # print("返回：")
            #         # print(ret.json())
            #         food_id = context.key_value["food_id"]
            #         try:
            #             sqlist.extend([
            #                 {"command": "delete from e_food where id={0}".format(int(food_id)), "db": "eatojoy"},
            #                 {"command": "delete from e_food_package where id={0}".format(int(food_id)), "db": "eatojoy"}
            #             ]),
            #         except:
            #             print('{0}参数为空，不执行SQL'.format('food_id'))
            #         for each in sqlist:
            #             exec_sql(each["command"], each["db"])
            #             print(str(each) + '执行TearDown成功！')
            #     else:
            #         # print("删除菜品失败")
            #         print(ret.json())

            if "vendor_id" in context.key_value.keys():

                sqlist = []
                print("封禁商家：")
                url = eatojoy_data.preData["eatojoy_url"] + "/admin/vendor/set_block"
                headers = {"eatojoy-admin-api-key": eatojoy_data.preData["eatojoy_bk_token"]}
                print("请求头：")
                print(headers)
                print("请求地址：" + url)
                data = {
                    "vendor_id": context.key_value["vendor_id"],
                    "on": 1
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.post(url, json=data, headers=headers)
                if str(ret.status_code).startswith("2"):
                    print("返回：")
                    print(ret.json())
                else:
                    print("封禁商家失败")
                    print(ret.json())

                # vendor_id = context.key_value["vendor_id"]
                # sqlist.extend([
                #     {"command": "delete from e_vendor where id={0}".format(int(vendor_id)), "db": "eatojoy"},
                #     {"command": "delete from e_vendor_protocol where vendor_id={0}".format(int(vendor_id)),
                #      "db": "eatojoy"},
                #     {"command": "delete from e_vendor_bank where vendor_id={0}".format(int(vendor_id)),
                #      "db": "eatojoy"}
                # ]),
                # for each in sqlist:
                #     exec_sql(each["command"], each["db"])
                #     print(str(each) + '执行TearDown成功！')

            if "admin_user_id" in context.key_value.keys():
                sqlist = []
                admin_user_id = context.key_value["admin_user_id"]
                sqlist.extend([
                    {"command": "delete from e_admin_users where id={0}".format(int(admin_user_id)), "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')

            # if "after_sales_id" in context.key_value.keys():
            #     sqlist = []
            #     after_sales_id = context.key_value["after_sales_id"]
            #     order_id = context.key_value["order_id"]
            #     sqlist.extend([
            #         {"command": "delete from e_after_sales_order where after_sales_id='{0}'".format(after_sales_id), "db": "eatojoy"},
            #         {"command": "delete from e_aftersales_action_log where order_id={0}".format(int(order_id)),"db": "eatojoy"}
            #     ]),
            #     for each in sqlist:
            #         exec_sql(each["command"], each["db"])
            #         print(str(each) + '执行TearDown成功！')

            # if "order_id" in context.key_value.keys():
            #     order_id = context.key_value["order_id"]
            #     if(int(context.key_value["order_id"]) % 100 < 10):
            #         order_table = "e_order_0" + str(int(context.key_value["order_id"]) % 100)
            #         order_table_detail = "e_order_detail_0" + str(int(context.key_value["order_id"]) % 100)
            #     else:
            #         order_table = "e_order_" + str(int(context.key_value["order_id"]) % 100)
            #         order_table_detail = "e_order_detail_" + str(int(context.key_value["order_id"]) % 100)
            #     sqlist.extend([
            #         {"command": "delete from {0} where order_id={1}".format(str(order_table),int(order_id)), "db": "eatojoy"},
            #         {"command": "delete from {0} where order_id={1}".format(str(order_table_detail), int(order_id)), "db": "eatojoy"}
            #     ]),
            #     for each in sqlist:
            #         exec_sql(each["command"], each["db"])

            if "user_group_id" in context.key_value.keys():
                sqlist = []
                user_group_id = context.key_value["user_group_id"]
                sqlist.extend([
                    {"command": "delete from e_admin_group where id={0}".format(int(user_group_id)), "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')


            if "coupon_activity_id" in context.key_value.keys():
                sqlist = []
                coupon_activity_id = context.key_value["coupon_activity_id"]
                sqlist.extend([
                    {"command": "delete from e_coupon_activity where id={0}".format(int(coupon_activity_id)), "db": "eatojoy"},
                    {"command": "delete from e_promotion_send_coupon_code where send_id={0} and type=2".format(int(coupon_activity_id)),
                     "db": "eatojoy"}
                ]),
                for each in sqlist:
                    exec_sql(each["command"], each["db"])
                    print(str(each) + '执行TearDown成功！')



            if "coupon_id" in context.key_value.keys():
                sqlist = []
                coupon_id = context.key_value["coupon_id"]
                result = []
                sqlist.extend([
                    {"command": "select coupon_code from e_promotion_coupon where id={0}".format(int(coupon_id)), "db": "eatojoy"},
                    {"command": "select coupon_status from e_promotion_coupon where id={0}".format(int(coupon_id)),
                     "db": "eatojoy"}
                ]),
                for each in sqlist:
                    result.append(str(exec_sql(each["command"], each["db"])))
                    print(str(each) + '执行TearDown成功！')

                coupon_code = re.findall('[a-zA-Z0-9]+',result[0])[0]

                coupon_status = re.findall('[a-zA-Z0-9]+', result[1])[0]

                if(coupon_status == 'pending' or coupon_status == 'failure'):
                    sqlist.extend([
                        {"command": "update e_promotion_coupon set is_deleted = 1 where id={0}".format(int(coupon_id)),
                         "db": "eatojoy"}
                    ]),
                    for each in sqlist:
                        result.append(str(exec_sql(each["command"], each["db"])))
                        print(str(each) + '执行TearDown成功！')
                else:
                    # print("停用优惠券券")
                    url = eatojoy_data.preData["eatojoy_url"] + "/admin/coupon/doinvalid"
                    headers = {"eatojoy-admin-api-key": eatojoy_data.preData["eatojoy_bk_token"]}
                    # print("请求头：")
                    # print(headers)
                    # print("请求地址：" + url)
                    data = {
                        "coupon_code": coupon_code
                    }
                    # print("请求参数：")
                    # print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    sqlist.extend([
                        {"command": "update e_promotion_coupon set is_deleted = 1 where id={0}".format(int(coupon_id)),
                         "db": "eatojoy"}
                    ]),
                    for each in sqlist:
                        result.append(str(exec_sql(each["command"], each["db"])))
                        print(str(each) + '执行TearDown成功！')
                    if str(ret.status_code).startswith("2"):
                        # print("返回：")
                        # print (ret.json())
                        pass
                    else:
                        print("停用优惠券失败")
                        print(ret.json())


            if "coupon_id_1" in context.key_value.keys():
                sqlist = []
                coupon_id = context.key_value["coupon_id_1"]
                result = []
                sqlist.extend([
                    {"command": "select coupon_code from e_promotion_coupon where id={0}".format(int(coupon_id)), "db": "eatojoy"},
                    {"command": "select coupon_status from e_promotion_coupon where id={0}".format(int(coupon_id)),
                     "db": "eatojoy"}
                ]),
                for each in sqlist:
                    result.append(str(exec_sql(each["command"], each["db"])))
                    print(str(each) + '执行TearDown成功！')

                coupon_code = re.findall('[a-zA-Z0-9]+',result[0])[0]

                coupon_status = re.findall('[a-zA-Z0-9]+', result[1])[0]

                if(coupon_status == 'pending' or coupon_status == 'failure'):
                    sqlist.extend([
                        {"command": "update e_promotion_coupon set is_deleted = 1 where id={0}".format(int(coupon_id)),
                         "db": "eatojoy"}
                    ]),
                    for each in sqlist:
                        result.append(str(exec_sql(each["command"], each["db"])))
                        print(str(each) + '执行TearDown成功！')
                else:
                    # print("停用优惠券券")
                    url = eatojoy_data.preData["eatojoy_url"] + "/admin/coupon/doinvalid"
                    headers = {"eatojoy-admin-api-key": eatojoy_data.preData["eatojoy_bk_token"]}
                    # print("请求头：")
                    # print(headers)
                    # print("请求地址：" + url)
                    data = {
                        "coupon_code": coupon_code
                    }
                    # print("请求参数：")
                    # print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    sqlist.extend([
                        {"command": "update e_promotion_coupon set is_deleted = 1 where id={0}".format(int(coupon_id)),
                         "db": "eatojoy"}
                    ]),
                    for each in sqlist:
                        result.append(str(exec_sql(each["command"], each["db"])))
                        print(str(each) + '执行TearDown成功！')
                    if str(ret.status_code).startswith("2"):
                        # print("返回：")
                        # print (ret.json())
                        pass
                    else:
                        print("停用优惠券失败")
                        print(ret.json())


            if "coupon_id_2" in context.key_value.keys():
                sqlist = []
                coupon_id = context.key_value["coupon_id_2"]
                result = []
                sqlist.extend([
                    {"command": "select coupon_code from e_promotion_coupon where id={0}".format(int(coupon_id)), "db": "eatojoy"},
                    {"command": "select coupon_status from e_promotion_coupon where id={0}".format(int(coupon_id)),
                     "db": "eatojoy"}
                ]),
                for each in sqlist:
                    result.append(str(exec_sql(each["command"], each["db"])))
                    print(str(each) + '执行TearDown成功！')


                coupon_code = re.findall('[a-zA-Z0-9]+',result[0])[0]

                coupon_status = re.findall('[a-zA-Z0-9]+', result[1])[0]

                sqlist.extend([
                    {"command": "update e_promotion_coupon set is_deleted = 1 where id={0}".format(int(coupon_id)),
                     "db": "eatojoy"}
                ]),
                for each in sqlist:
                    result.append(str(exec_sql(each["command"], each["db"])))
                    print(str(each) + '执行TearDown成功！')
            else:
                # print("停用优惠券券")
                if(coupon_status == 'pending' or coupon_status == 'failure'):

                    url = eatojoy_data.preData["eatojoy_url"] + "/admin/coupon/doinvalid"
                    headers = {"eatojoy-admin-api-key": eatojoy_data.preData["eatojoy_bk_token"]}
                    # print("请求头：")
                    # print(headers)
                    # print("请求地址：" + url)
                    data = {
                        "coupon_code": coupon_code
                    }
                    # print("请求参数：")
                    # print(decode_str(data))
                    ret = requests.post(url, json=data, headers=headers)
                    sqlist.extend([
                        {"command": "update e_promotion_coupon set is_deleted = 1 where id={0}".format(int(coupon_id)),
                         "db": "eatojoy"}
                    ]),
                    for each in sqlist:
                        result.append(str(exec_sql(each["command"], each["db"])))
                        print(str(each) + '执行TearDown成功！')
                    if str(ret.status_code).startswith("2"):
                        # print("返回：")
                        # print (ret.json())
                        pass
                    else:
                        print("停用优惠券失败")
                        print(ret.json())


        elif "ALL_APP_HOTEL" in folder:
            from TestData import hotel_data

            if "order_id" in context.key_value.keys():
                print("取消预定订单：")
                url = hotel_data.preData["hotel_url"] + "/order/cancel"
                if context.key_value["token"] != '':
                    headers = {"token": context.key_value["token"],
                               "client":"IOS",

                               }
                else:
                    headers = {"token": hotel_data.preData["hotel_token"],
                               "client": "IOS",

                               }
                print("请求头：")
                print(headers)
                print("请求地址：" + url)
                data = {
                    "order_sn": context.key_value["order_id"]
                }
                print("请求参数：")
                print(decode_str(data))
                ret = requests.get(url, json=data, headers=headers)
                if str(ret.status_code).startswith("2"):
                    print("返回：")
                    print(ret.json())
                    if ret.json()["status"] == False:
                        print("获取退订订单详情：")
                        url = hotel_data.preData["hotel_url"] + "/order/getUnsubscribe"
                        if context.key_value["token"] != '':
                            headers = {"token": context.key_value["token"],
                                       "client": "IOS",
                                       }
                        else:
                            headers = {"token": hotel_data.preData["hotel_token"],
                                       "client": "IOS",
                                       }
                        print("请求头：")
                        print(headers)
                        print("请求地址：" + url)
                        data = {
                            "order_sn": context.key_value["order_id"]
                        }
                        print("请求参数：")
                        print(decode_str(data))
                        ret = requests.get(url, json=data, headers=headers)

                        print("返回：")
                        print(ret.json())

                        room_id = ret.json()["data"]["roomInfo"][0]['list'][0]["roomId"]

                        print("退订订单：")
                        url = hotel_data.preData["hotel_url"] + "/order/unsubscribe"
                        if context.key_value["token"] != '':
                            headers = {"token": context.key_value["token"],
                                       "client": "IOS",
                                       }
                        else:
                            headers = {"token": hotel_data.preData["hotel_token"],
                                       "client": "IOS",
                                       }
                        print("请求头：")
                        print(headers)
                        print("请求地址：" + url)
                        data = {
                            "order_sn": context.key_value["order_id"],
                            "rooms":room_id,
                            "reasonType":"1"
                        }
                        print("请求参数：")
                        ret = requests.post(url, json=data, headers=headers)

                        print("返回：")
                        print(ret.json())



                else:
                    print("取消预定订单失败")
                    print(ret.json())



            # if "floor_id" in context.key_value.keys():
            #
            #     sqlist = []
            #     floor_id = context.key_value["floor_id"]
            #     sqlist.extend([
            #         {"command": "DELETE from floor where id = {0}".format(floor_id),
            #          "db": "hotel"}
            #     ]),
            #     for each in sqlist:
            #         exec_sql(each["command"], each["db"])
            #         print(str(each) + '执行TearDown成功！')
            #
            #
            # if "roomtype_id" in context.key_value.keys():
            #
            #     sqlist = []
            #     roomtype_id = context.key_value["roomtype_id"]
            #     sqlist.extend([
            #         {"command": "DELETE from room_type where id = {0}".format(roomtype_id),
            #          "db": "hotel"}
            #     ]),
            #     for each in sqlist:
            #         exec_sql(each["command"], each["db"])
            #         print(str(each) + '执行TearDown成功！')
            #
            #
            #
            #
            # if "hotel_id" in context.key_value.keys():
            #
            #     sqlist = []
            #     hotel_id = context.key_value["hotel_id"]
            #     sqlist.extend([
            #         {"command": "DELETE from hotel where id = {0}".format(hotel_id),
            #          "db": "hotel"}
            #     ]),
            #     for each in sqlist:
            #         exec_sql(each["command"], each["db"])
            #         print(str(each) + '执行TearDown成功！')





    except Exception as e:
        print(e)
        traceback.print_exc()
        print(sqlist)


class Context(object):
    """
    Define the Context to store the return value.
    """
    def __init__(self):
        self.key_value = {}


