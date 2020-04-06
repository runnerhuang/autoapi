# -*- coding: utf-8 -*-
# @Date  : 2018/8/2 下午4:27
# @Author: Runner
# @Desc  : Read config data, project,db,email,url

import os
import configparser

folder = os.environ.get('PROJECT_CASE_FOLDER', 'TestCase//BAIDU//ALL//ALL')
item = os.environ.get('NUMBER', 0)
sleeptime = float(os.environ.get('SLEEP_TIME', 0))
items = os.environ.get("TESTCASES", "")
td = os.environ.get("TEARDOWN", 1)
email = os.environ.get('EMAIL', 0)
env = os.environ.get("ENV", 'test')
dataready = os.environ.get('DATAREADY', 0)
rr = os.environ.get("RERUN", 0)
lp = os.environ.get("LOOP", 0)
method = os.environ.get('METHOD', "DEBUG")
testlist = os.environ.get("TESTLIST", "")

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
