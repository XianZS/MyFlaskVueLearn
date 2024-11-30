import sys

from views import ManageApi


class _Url_ManageApi:
    def __init__(self, flaskApp):
        flaskApp.add_url_rule(
            '/ManageApi',
            view_func=ManageApi.as_view('ManageApi'),
            methods=['get']
        )


class UrlsApi:
    def __init__(self, flaskApp):
        self.api = _Url_ManageApi(flaskApp)
