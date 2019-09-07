import urllib3
import json


class request_manage(object):

    def __init__(self):
        pass

    def sen_post_dingtalk_message(self, message):
        message_str = message

        if type(message) != str:
            print('不是dict')
            message_str = str(message)

        http = urllib3.PoolManager()
        rq_data = {'msgtype': 'text', 'text': {"content": message_str}}
        rq_url = 'https://oapi.dingtalk.com/robot/send?access_token=0b9390026affabf03dec851cfc64f24a2319f2259fa7281f7840f2a38fcab829'
        encoded_data = json.dumps(rq_data).encode('utf-8')
        rq_header = {'Content-Type: application/json'}
        rq = http.request('POST', rq_url, body=encoded_data, headers=rq_header)
        print(rq.data.decode())

    # urllib3.disable_warnings()
    # url = "www.baidu.com"
    # http = urllib3.PoolManager()
    # rq_data = {'msgtype': 'text', 'text': {"content": "我就是我, 是不一样的烟火"}}
    # data = {'attribute': 'value'}
    # encoded_data = json.dumps(rq_data).encode('utf-8')
    # r = http.request('POST', 'https://oapi.dingtalk.com/robot/send?access_token=0b9390026affabf03dec851cfc64f24a2319f2259fa7281f7840f2a38fcab829', body=encoded_data, headers={'Content-Type': 'application/json'})
    # print(r.data.decode())

    # http = urllib3.PoolManager()
    # rq_data = {'msgtype': 'text', 'text': {"content": "我就是我, 是不一样的烟火"}}
    # rq_url = 'https://oapi.dingtalk.com/robot/send?access_token=0b9390026affabf03dec851cfc64f24a2319f2259fa7281f7840f2a38fcab829'
    # encoded_data = json.dumps(rq_data).encode('utf-8')
    # # encoded_data = json.dumps(data).encode('utf-8')
    # rq_header = {'Content-Type: application/json'}
    # rq = http.request('POST', rq_url, body=encoded_data, headers={'Content-Type': 'application/json'})
    # print(rq.data.decode())
