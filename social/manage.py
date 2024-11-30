"""
    导入第三方包
"""
from flask import Flask, jsonify, request

# 跨域，因为浏览器的同源策略，不允许跨域访问
from flask_cors import CORS
from sqlalchemy import text
# 类视图
from flask.views import MethodView

"""
    导入自定义包
"""
from database import db, r
from config import conn
from RecordSqlLine import sqlApi

# 实例化 flask 对象
app = Flask(__name__)

# 配置转码
# 禁止 json 编码为 ascii
app.config['JSON_AS_ASCII'] = False
# 配置 mysql 数据库
app.config[
    "SQLALCHEMY_DATABASE_URI"] = (f"{conn.mysql_type}://"
                                  f"{conn.mysql_user}:{conn.mysql_password}"
                                  f"@{conn.mysql_host}:{conn.mysql_post}"
                                  f"/{conn.mysql_database}")
# 设置 mysql 自动提交代码
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 初始化操作
db.init_app(app)
# 配置跨域
CORS(app, cors_allowed_origins="*")

from urls import UrlsApi

UrlsApi = UrlsApi(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
