import json
from wsgiref.simple_server import make_server

import colorama


def response(code, msg):
    data = {
        'code': code,
        'message': msg
    }

    return json.dumps(data)


def do_event(event, req_data):
    """
    ipcc通知处理
    :param event: 事件类型
    :param req_data: 请求数据
    :return:
    """
    if event == "incomingcallack":
        print(colorama.Back.BLUE + "INFO", "呼入请求-> ", req_data)

    elif event == "callstatrpt":
        print(colorama.Back.BLUE + "INFO", "号码呼叫结果-> ", req_data)

    elif event == "vadStart":
        print(colorama.Back.BLUE + "INFO", "检测到用户说话-> ", req_data)

    elif event == "asrNotice":
        print(colorama.Back.BLUE + "INFO", "asr识别结果通知-> ", req_data)

    elif event == "playoverrpt":
        print(colorama.Back.BLUE + "INFO", "语音播放结束通知-> ", req_data)

    elif event == "multrpt":
        print(colorama.Back.BLUE + "INFO", "多语音播放结束通知-> ", req_data)

    elif event == "calldisconnectrpt":
        print(colorama.Back.BLUE + "INFO", "挂机通知-> ", req_data)

    elif event == "callbillrpt":
        print(colorama.Back.BLUE + "INFO", "话单通知-> ", req_data)

    elif event == "calldisconnectrpt":
        print(colorama.Back.BLUE + "INFO", "挂机通知-> ", req_data)

    elif event == "calldisconnectrpt":
        print(colorama.Back.BLUE + "INFO", "挂机通知-> ", req_data)

    else:
        print(colorama.Back.BLUE + "INFO", "未知通知-> ", req_data)


def handler_callback(environ, start_response):

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    if request_body_size > 0:
        request_body = environ['wsgi.input'].read(request_body_size)

        req_data = json.loads(request_body.decode('utf8'))
        event = req_data.get("event")
        do_event(event, req_data)

    start_response('200 OK', [('Content-Type', 'application/json')])

    res = response("0", "0")

    return [bytes(res, encoding="utf-8")]


def app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']

    if method == "POST" and path == "/v1/ipcc/callback":

        return handler_callback(environ, start_response)

    start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    return []


httpd = make_server("", 8080, app)
colorama.init(autoreset=True)
print(colorama.Back.BLUE + "INFO", "http server running...")


