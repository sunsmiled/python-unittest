# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

import unittest


class TestDemo(unittest.TestCase):
    def test_one(self):
        print("第一条case")

    def test_two(self):
        print("第二条case")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo('test_one'))
    suite.addTest(TestDemo('test_two'))
    unittest.TextTestRunner().run(suite)
    