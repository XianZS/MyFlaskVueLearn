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

    # 测试有参数 post 接口
    def test_post(self, input_url, input_data):
        self.url = input_url
        self.data = input_data
        # 对于 post 请求而言，测试文件中的传入参数应该为 data
        res_text = requests.post(self.url, data=self.data)
        return res_text.text

    # 测试无参数 post 接口
    def test_post_no_params(self, input_url):
        self.url = input_url
        res_text = requests.post(self.url)
        return res_text.text

    # 测试有参数 get 接口
    def test_get(self, input_url, input_data):
        self.url = input_url
        self.data = input_data
        # 对于 get 请求而言，测试文件中的传入参数应该为 params
        res_text = requests.get(self.url, params=self.data)
        return res_text.text

    # 测试无参数 get 接口
    def test_get_no_params(self, input_url):
        self.url = input_url
        res_text = requests.get(self.url)
        return res_text.text


if __name__ == '__main__':
    HttpApi = HttpApiTest()
    url = "http://192.168.71.98:5000/user_view/"
    x = HttpApi.test_get(url, {"email": "3135989009@qq.com"})
    print(x)
