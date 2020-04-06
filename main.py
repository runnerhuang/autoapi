import os
from argparse import ArgumentParser

ap = ArgumentParser(
    description='Automation API Test.'
)

ap.add_argument('-F', dest='project_case_folder', action='store', type=str, nargs='?',
                default='TestCase//BAIDU//ALL//ALL')
ap.add_argument('-N', dest='number', action="store", type=int, nargs='?', default='0')  # 单例，0-all
ap.add_argument('-S', dest='sleep_time', action="store", type=float, nargs='?', default=0)
ap.add_argument('-TC', dest='testcases', action="store", type=str, nargs='?', default="")  # 多例
ap.add_argument('-TD', dest="teardown", action="store", type=int, nargs='?', default=1)  # 是否运行teardown,默认1不执行
ap.add_argument('-E', dest="email", action="store", type=int, nargs="?", default=1)  # 0不发email，非0发
ap.add_argument('-ENV', dest="env", action="store", type=str, nargs='?', default='test')  # run env
ap.add_argument('-DR', dest="dataready", action="store", type=int, nargs='?', default=0)  # 是否在用例执行前准备数据
ap.add_argument('-RR', dest="rerun", action="store", type=int, nargs='?', default=0)  # 是否重跑并重跑几次
ap.add_argument('-LP', dest="loop", action="store", type=int, nargs='?', default=0)  # 循环执行次数
ap.add_argument('-MD', dest='method', action="store", type=str, nargs='?', default="DEBUG")
ap.add_argument('-L', dest="list", action="store", type=str, nargs='?', default="1")  # TODO
# ap.add_argument('-DB', dest='database', action="store", type=str, nargs='?', default="waiwang")  # TODO

args = ap.parse_args()

os.environ.setdefault('PROJECT_CASE_FOLDER', args.project_case_folder)
os.environ.setdefault('NUMBER', str(args.number - 1))
os.environ.setdefault('SLEEP_TIME', str(args.sleep_time))
os.environ.setdefault('TESTCASES', args.testcases)
os.environ.setdefault('TEARDOWN', str(args.teardown))
os.environ.setdefault('EMAIL', str(args.email))
os.environ.setdefault('ENV', str(args.env))
os.environ.setdefault('DATAREADY', str(args.dataready))
os.environ.setdefault('RERUN', str(args.rerun))
os.environ.setdefault('LOOP', str(args.loop))
os.environ.setdefault('METHOD', args.method)
os.environ.setdefault('TESTLIST', args.list)
# os.environ.setdefault('DATABASE', args.database)

try:
    if os.path.isfile("log.txt"):
        os.remove("log.txt")
    from TestRunner.testRunner import TestRunner

    TestRunner.run()
except Exception as e:
    print(e)
