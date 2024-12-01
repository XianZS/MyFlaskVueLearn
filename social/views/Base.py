from flask.views import MethodView


class Base(MethodView):
    def get(self):
        return "True"
