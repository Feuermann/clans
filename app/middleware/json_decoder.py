import json
import falcon


class JSONDecoder(object):

    def process_request(self, req, res):
        if req.content_type == 'application/json':
            try:
                raw_json = req.stream.read()
            except Exception:
                message = 'Read Error'
                raise falcon('Bad request', message)
            try:
                req.context['data'] = json.loads(raw_json.decode('utf-8'))
            except ValueError:
                raise ValueError('No JSON object could be decoded or Malformed JSON')
            except UnicodeDecodeError:
                raise Exception('Cannot be decoded by utf-8')
        else:
            req.context['data'] = None