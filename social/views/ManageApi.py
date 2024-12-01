from .Base import Base

from flask import jsonify


class ManageApi(Base):
    def get(self):
        return jsonify({"code": 200, "msg": "ok"})
