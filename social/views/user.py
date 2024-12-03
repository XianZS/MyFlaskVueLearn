# -*- coding: UTF-8 -*-
"""
    @Project : MyFlaskVueLearn 
    @File    : user.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/2 19:29 
    @NowThing: 
"""

from flask import Blueprint, request, jsonify
from social.utils import check_re, SaveCode, CreateCode, SendEmail

user_view = Blueprint('user_view', __name__)


@user_view.route('/', methods=['GET'])
def index():
    _email = request.args.get('email', None)
    if check_re(_email):
        s = SendEmail()
        msg = CreateCode(False, 6).return_code()
        send_judge = s.send_mail(_email, "验证码", "您社交平台的验证码为 : " + msg)
        if not send_judge:
            # 判断是否发送成功
            return jsonify({"code": 0, "msg": "邮箱发送失败"})
        SaveCode_class = SaveCode()
        SaveCode_class.save_code(_email, msg, 300)
        some = SaveCode_class.show_code(_email)
        # 判断发送成功
        return jsonify({'code': 200, 'msg': '邮箱格式正确', "验证码": some})
    else:
        return jsonify({'code': 400, 'msg': '邮箱格式错误'})


@user_view.route('/show/')
def show():
    return "/user_view/show/"
