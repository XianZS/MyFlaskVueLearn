# 导包
from flask import Flask, jsonify

# 跨域，因为浏览器的同源策略，不允许跨域访问
from flask_cors import CORS
from sqlalchemy import text

from database import db
from config import conn

# 实例化 flask 对象
app = Flask(__name__)

# 配置转码
# 禁止 json 编码为 ascii
app.config['JSON_AS_ASCII'] = False
# 配置 mysql 数据库
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://social:YangHaiTao3135@39.100.73.172:3306/social"
# 设置 mysql 自动提交代码
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 初始化操作
db.init_app(app)
# 配置跨域
CORS(app, cors_allowed_origins="*")


# 配置路由

@app.route('/', methods=['GET'])
def index():
    return "首页"


@app.route('/find', methods=['GET'])
def find():
    myId = db.session.execute(text("select * from User")).fetchall()
    return jsonify({"data": [list(x) for x in myId]})


@app.route('/update', methods=['GET'])
def update():
    db.session.execute(text("update User set UserName='iom' where UserId=1001"))
    db.session.commit()
    return "True"


@app.route('/delete', methods=['GET'])
def delete():
    db.session.execute(text("delete from User where UserId=1001"))
    db.session.commit()
    return "True"


@app.route('/insert', methods=['Get', 'POST'])
def insert():
    db.session.execute(text("insert into User (UserId,UserName,UserAddress) values (1010,'pom','云南')"))
    db.session.commit()
    return "true"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
