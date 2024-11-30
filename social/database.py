# 数据库示例文件
import redis
from flask_sqlalchemy import SQLAlchemy
import pymysql

# 通过 pymysql 来模拟 mysqldb
pymysql.install_as_MySQLdb()

# 实例化 mysql 对象
db = SQLAlchemy()
r = redis.Redis(host='39.100.73.172',
                port=6379,
                db=0,
                decode_responses=True,
                password='YangHaiTao3135')
