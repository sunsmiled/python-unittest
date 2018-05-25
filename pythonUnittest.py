# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

import requests
import json
url = "http://m.imooc.com/passport/user/login"
data = {"username": "158****4609", "password": "111111", "verify": "", "referer": "http://imooc.com"}
res = requests.post(url, data).json()
print(res)


class RunMethod:
    def post_main(self, url=None, data=None):
        res = None
        res = requests.post(url=url, data=data).json()
        return res

    def get_mait(self, url, data):
        res = None
        res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, method, url=None, data=None):
        res = None
        if method == "Post":
            res = self.post_main(url, data)
        else:
            res = self.get_mait(url, data)
        return res


if __name__ == '__main__':
    data = {"username": "158****4609", "password": "111111", "verify": "", "referer": "http:"}
    t = RunMethod()
    print(t.run_main('Post', 'http://m.imooc.com/passport/user/login'), data)
