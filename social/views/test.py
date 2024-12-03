# -*- coding: UTF-8 -*-
"""
    @Project : MyFlaskVueLearn 
    @File    : test.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/2 19:59 
    @NowThing: 
"""
from flask import Blueprint, request, jsonify
from flask.views import MethodView

# 创建蓝图对象
test_view = Blueprint('test_view', __name__)

"""
    创建 view
"""


@test_view.route('/test/', methods=['GET'])
def test_get():
    return "test_get"


@test_view.route('/test/', methods=['POST'])
def test_post():
    return "test_post"


@test_view.route('/show/')
def show():
    return "show"
