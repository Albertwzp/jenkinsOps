#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner
# https://www.cnblogs.com/xiaoxiaolvdou/p/9503090.html
s = unittest.TestSuite()
# 1.调用addTest来加载测试用例：类名(‘方法名’)的集合
#s.addTests([Test_JenkinsOps("test_Get_view"),Test_jenkinsOps("test_Get_job")])

# 2.实例化TestLoader的对象
loader = unittest.TestLoader()
# 使用discover()去找一个目录下的所有测试用例的文件,并将返回数据添加到测试套件中
s.addTests(loader.discover(os.getcwd()))
#fs = open("test_run_report.txt","w")
#runner = unittest.TextTestRunner(fs)
fp = open(os.getcwd() +"/test_report.html","wb")
runner = HTMLTestRunner(stream=fp, title="title", description="desc", tester="tester")
runner.run(s)
