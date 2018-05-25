# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

import unittest
from pythonUnittest import RunMethod
import HTMLTestRunner


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.run_method = RunMethod()

    def test_one(self):
        print("第一条case")
        data = {}
        res = self.run_method.run_main('Post', '')
        print(res)

    def test_two(self):
        print("第二条case")
        data = {}
        res = self.run_method.run_main('get', '')
        print(res)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo('test_one'))
    suite.addTest(TestDemo('test_two'))
    # 定义报告路径
    filename = 'test.html'
    # 定义报告文件权限，wb，表示有读写权限
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='SaraTest',
        description='测试报告')
    # 执行测试
    runner.run(suite)
    # 关闭文件，否则会无法生成文件
    fp.close()
