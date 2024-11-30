from flask.views import MethodView


class ManageApi(MethodView):
    def get(self):
        return "True"
