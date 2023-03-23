from flask import Flask, request, g, jsonify
import json
import requests
import action_utils
import listener

setu_api = Flask(__name__)

@setu_api.route('/', methods = ['POST'])
def post_data():
    try:
        data = dict(json.loads(request.data.decode()))
        print(data)
        if data.get('meta_event_type', None) is not None:
            listener.restart_judge()
            return b'', 200
        else:
            listener.update_last_time()
            action_utils.action_follow_rec(data)
            print(data)
        return b'', 200
    except Exception as e:
        print("error", str(e))
        return b'', 200

if __name__ == '__main__':
    setu_api.run(host = '127.0.0.1', port = '8080')
    # r = requests.post('http://127.0.0.1:5701', data = {"msg":1, "group_id":2})
    # print(r.content)


