"""
    Flask 接口测试
    @author: XianZS
"""
import this
from tkinter.font import names

import requests


class HttpApiTest:
    def __init__(self):
        self.url = ''
        self.data = {}

    # 测试 post 接口
    def test_post(self, input_url, input_data):
        self.url = input_url
        self.data = input_data
        # 对于 post 请求而言，测试文件中的传入参数应该为 data
        res_text = requests.post(self.url, data=self.data)
        return res_text.text

    # 测试 get 接口
    def test_get(self, input_url, input_data):
        self.url = input_url
        self.data = input_data
        # 对于 get 请求而言，测试文件中的传入参数应该为 params
        res_text = requests.get(self.url, params=self.data)
        return res_text.text


if __name__ == '__main__':
    HttpApi = HttpApiTest()
    # 输入 url
    test_url = input("请输入测试的 url 地址：")
    # 请输入传入参数
    test_email, test_passwd = input("请输入邮箱和密码").split()
    res = HttpApi.test_post(test_url, {"email": test_email, "password": test_passwd})
    print(res)
