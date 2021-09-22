#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

projectname = 'jenkinsOps'
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[0: curPath.rindex(projectname)] + projectname
sys.path.append(rootPath)

from jenkinsOps import jenkins_ops

class Test_jenkinsOps(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.ops = jenkins_ops.JenkinsOps('http://localhost:8080/', username='user', password='passwd')
    @classmethod
    def tearDown(self):
        print("Test Finish")

    def test_Get_view(self):
        self.assertEqual(self.ops.get_view_list(), None)
    def test_Get_job(self):
        self.assertEqual(self.ops.get_job_list(view="wyc"), None)
    def test_Get_job_param(self):
        self.assertEqual(self.ops.get_job_param(name="wyc"), None)

if __name__ == '__main__':
    unittest.main()
