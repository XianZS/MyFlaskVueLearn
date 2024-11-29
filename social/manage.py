# 导包
from flask import Flask, jsonify

# 跨域，因为浏览器的同源策略，不允许跨域访问
from flask_cors import CORS
from sqlalchemy import text

from database import db

# 实例化 flask 对象
app = Flask(__name__)

# 配置转码
# 禁止 json 编码为 ascii
app.config['JSON_AS_ASCII'] = False
# 配置 mysql 数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://social:YangHaiTao3135@39.100.73.172:3306/social"
# 设置 mysql 自动提交代码
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# 初始化操作
db.init_app(app)
# 配置跨域1
CORS(app, cors_allowed_origins="*")


# 配置路由

@app.route('/', methods=['GET'])
def index():
    myId = db.session.execute(text("select * from User")).fetchall()
    return jsonify({"data": [list(x) for x in myId]})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
