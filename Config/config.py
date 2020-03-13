# -*- coding: utf-8 -*-
# @Date  : 2018/8/2 下午4:27
# @Author: Runner
# @Desc  : Read config data, project,db,email,url

import os
import configparser

item = os.environ.get('UT_ITEM', 0)
items = os.environ.get("CASELIST", "")
testlist = os.environ.get("testlist", "")
td = os.environ.get("teardown", 1)
method = os.environ.get('METHOD', "DEBUG")
folder = os.environ.get('projectCaseFolder', 'TestCase//ERP')
env = os.environ.get("env", 'test')
email = os.environ.get('email', 0)
dataready = os.environ.get('dataready', 0)
rr = os.environ.get("rerun", 0)
lp = os.environ.get("loop", 0)

time = []  # 每个用例执行的时间
reruns = []  # 每个用例重复执行的次数


class ReadConfig:
    # get the ini file path
    cur_path = os.path.abspath(os.path.dirname("__file__"))
    if cur_path.find("Config") == -1:
        cur_path = os.path.join(cur_path, 'Config')
    conf_path = os.path.join(cur_path, '{0}_{1}.ini'.format(folder.split("//")[1].lower(), env))
    conf = configparser.ConfigParser()
    conf.read(conf_path, encoding="utf-8")

    @classmethod
    def get_project(cls, name):
        value = cls.conf.get("project_info", name)
        return value

    @classmethod
    def get_db(cls, name):
        value = cls.conf.get("test_db", name)
        return value

    @classmethod
    def get_email(cls, name):
        value = cls.conf.get("email_info", name)
        return value

    @classmethod
    def get_url(cls, name):
        value = cls.conf.get("url", name)
        return value

