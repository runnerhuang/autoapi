# -*- coding: utf-8 -*-
import requests
from Config import config

way = config.method


def request_data(url, method, param=None, **kwargs):

    ret = None

    if way == "DEBUG" or way == "debug":
        if method == "POST" or method == "post":
            ret = requests.post(url, param, **kwargs)
        elif method == "GET" or method == "get":
            ret = requests.get(url, param, **kwargs)
        elif method == "DELETE" or method == "delete":
            ret = requests.delete(url, **kwargs)
        elif method == "PUT" or method == "put":
            ret = requests.put(url, json=param, **kwargs)
        elif method == "PATCH" or method == "patch":
            ret = requests.patch(url, param, **kwargs)
        if ret.status_code == 500:
            return "Server Internal Error 500"
        if ret.status_code == 404:
            return "Cannot find the page, 404"
        else:
            try:
                return ret.json()
            except:
                return ret.text


def restful_api(req_url, req_method, params=None, files=None, headers=None, cookies=None):
    ret = None
    if req_method == "POST" or req_method == "post":
        if files:
            ret = request_data(req_url, req_method, params, files=files, headers=headers, cookies=cookies,
                               allow_redirects=False)
        elif headers and "Content-Type" in headers.keys():
            if "x-www-form-urlencoded" in headers["Content-Type"]:
                ret = request_data(req_url, req_method, params,  headers=headers, cookies=cookies,
                                   allow_redirects=False)
            else:
                ret = request_data(req_url, req_method, json=params, files=files, headers=headers, cookies=cookies,
                                   allow_redirects=False)
        else:
            ret = request_data(req_url, req_method, json=params, files=files, headers=headers, cookies=cookies,
                               allow_redirects=False)
    elif req_method == "delete":
        ret = request_data(req_url, req_method, json=params, headers=headers, cookies=cookies, allow_redirects=False)
    else:
        ret = request_data(req_url, req_method, params, headers=headers, cookies=cookies, allow_redirects=False)
    return ret


