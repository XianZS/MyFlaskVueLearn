# -*- coding: UTF-8 -*-
"""
    @Project : MyFlaskVueLearn 
    @File    : login.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/5 15:38 
    @NowThing: 
"""
from flask import Blueprint

login_views = Blueprint('login', __name__)


# 创建分支路由
# 点击登陆按钮，跳转到登陆页面
@login_views.route('/login', methods=['GET'])
def login_get():
    return "login"


# 点击登陆按钮，将用户信息提交到后台
@login_views.route('/login', methods=['POST'])
def login_post():
    return "login"


@login_views.route('/logout', methods=['GET', 'POST'])
def loginout_get_post():
    return "logout"
