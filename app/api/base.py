import falcon
import json

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

from urllib.parse import parse_qsl


class BaseResource(object):
    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def on_error(self, res, error=None):
        res.status = error['status']
        meta = OrderedDict()
        meta['code'] = error['code']
        meta['message'] = error['message']

        obj = OrderedDict()
        obj['meta'] = meta
        res.body = self.to_json(obj)

    def on_success(self, res, data=None, status=None):
        if status:
            stat = status
        else:
            stat = falcon.HTTP_200
        res.status = stat
        meta = OrderedDict()
        code, message = (stat.split(" ", 1))
        meta['code'] = code
        meta['message'] = message

        obj = OrderedDict()
        obj['meta'] = meta
        obj['data'] = data
        res.body = self.to_json(obj)

    def get_query_params(self, request):
        params = dict(parse_qsl(request.query_string))
        return params
