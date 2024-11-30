"""
    SQL 语句记录器
    @author: XianZS
"""
import sys
import os
from datetime import datetime


class RecordSqlLine(object):
    def __init__(self):
        self.FilePath = "../logs/SQL_Logs.txt"

    def read(self):
        with open(self.FilePath, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, sql_line):
        with open(self.FilePath, "a", encoding="utf-8") as f:
            f.write(str(datetime.now()) + " : " + sql_line + "\n")
            return "true"


sqlApi = RecordSqlLine()
