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
    __urls_dict = dict()

    def __init__(self, flaskApp):
        self.__urls_dict = {
            '/ManageApi': _Url_ManageApi(flaskApp)
        }
