# 数据库示例文件

from flask_sqlalchemy import SQLAlchemy
import pymysql

# 通过 pymysql 来模拟 mysqldb
pymysql.install_as_MySQLdb()

# 实例化 mysql 对象
db = SQLAlchemy()
