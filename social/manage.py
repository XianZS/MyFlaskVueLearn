"""
    导入第三方包
"""
import sys

sys.path.append("..")
from flask import Flask

# 跨域，因为浏览器的同源策略，不允许跨域访问
from flask_cors import CORS
# 类视图
# 导入蓝图模块
from views import login_views

"""
    导入自定义包
"""
from database import db
from config import conn

"""
    【1】 Flask 对象初始化
"""
app = Flask(__name__)
# 配置转码
# 禁止 json 编码为 ascii
app.config['JSON_AS_ASCII'] = False
"""
    【2】 数据库链接初始化
"""
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

"""
    【3】 蓝图初始化；url 与 view 绑定关系添加到 app 之中
"""
app.register_blueprint(login_views, url_prefix="/login")
"""
    【4】 跨域初始化，绑定 vue
"""
CORS(app, cors_allowed_origins="*")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
