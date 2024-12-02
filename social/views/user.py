# -*- coding: UTF-8 -*-
"""
    @Project : MyFlaskVueLearn 
    @File    : user.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/2 19:29 
    @NowThing: 
"""

from flask import Blueprint

user_view = Blueprint('user_view', __name__)


@user_view.route('/')
def index():
    return "user_view"


@user_view.route('/show/')
def show():
    return "/user_view/show/"
