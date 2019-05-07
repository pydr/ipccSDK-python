import json

from ipcc.request import Request


class Client(object):

    def __init__(self, host, appid):
        self.host = host
        self.appid = appid
        print("sdk init success...")

    def out_call(self, caller, called, timeout=40, ai=1, **kwargs):
        """
        发起呼叫
        :param caller: 主叫号码， 联系腾讯云获取
        :param called: 被叫号码
        :param timeout: 呼叫超时事件(20-60s)
        :param ai: 是否启用asr模块, 默认启用
        :return:
        """
        url = self.host + '/ipcc/call/outCall'

        req_data = {
            'appId': self.appid,
            'caller': caller,
            'called': called,
            'timeout': timeout,
            'AiFlag': ai
        }

        for key, value in kwargs.items():
            req_data[key] = value

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)
        code = response["code"]
        callid = response['callId']

        return code, callid

    def notify(self, caller, called, text):
        """
        发起通知型呼叫
        :param caller: 主叫号码， 联系腾讯云获取
        :param called: 被叫号码
        :param text: 需要播放的内容文本
        :return: 会话id
        """
        url = self.host + '/ipcc/call/callNotifyV2'

        play_data = {
            'voice': text,
            'flag': 0
        }

        req_data = {
            'appId': self.appid,
            'caller': caller,
            'called': called,
            'voices': [play_data]
        }

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)

        code = response["code"]
        callid = response["callId"]

        return code, callid

    def hungup(self, callid):
        """
        挂机
        :param callid:
        :return:
        """
        url = self.host + "/ipcc/call/disConnect"

        req_data = {
            'appId': self.appid,
            'callId': callid
        }

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)

        return response

    def play(self, callid, flag, voice, get_key=0, play_times=1, **kwargs):
        """
        播放tts语音
        :param callid: 会话id,发起呼叫成功后返回
        :param get_key: 是否获取按键事件， 默认不获取
        :param play_times: 语音播放次数，默认1次
        :param flag: 语音类型, 0->tts, 1->录音
        :param voice: 需要播放内容(tts->语音文本, 录音->录音文件路径)
        :param data: 会话标识
        :return:
        """
        url = self.host + "/ipcc/call/play"

        req_data = {
            'appId': self.appid,
            'callId': callid,
            'getKey': get_key,
            'flag': flag,  # 0:播放tts, 1: 播放录音
            'voiceStr': voice,
            'playTime': play_times,  # 播放次数
        }

        for key, value in kwargs.items():
            req_data[key] = value

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)
        code = response['code']
        callid = response['callId']

        return code, callid

    def stop_play(self, callid, **kwargs):
        """
        停止当前语音播放,用于打断通话
        :param callid: 会话id,发起呼叫成功后返回
        :return:
        """
        url = self.host + "/ipcc/call/stoPlay"

        req_data = {
            'appId': self.appid,
            'callId': callid
        }

        for key, value in kwargs.items():
            req_data[key] = value

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)
        code = response["code"]
        callid = response["callId"]

        return code, callid

    def transfer(self, callid, called, voice, **kwargs):
        """
        呼叫转接
        :param callid: 会话id, 发起呼叫成功后返回
        :param called: 转接的目标电话
        :param voice: 播放的语音文件
        :return:
        """
        url = self.host + "/ipcc/call/transfer"

        req_data = {
            'appId': self.appid,
            'callId': callid,
            'called': called,
            'fileName': voice
        }

        for key, value in kwargs.items():
            req_data[key] = value

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)
        code = response['code']
        callid = response['callid']

        return code, callid

    def multi_play(self, callid, orders, play_times=1):
        """
        播放多段语音
        :param callid: 会话id
        :param play_times: 播放次数
        :param orders: 播放信息列表
        :return:
        """
        url = self.host + "/ipcc/call/multOrders"

        req_data = {
            'appId': self.appid,
            'callId': callid,
            'playtime': play_times,
            'orders': orders
        }

        headers = {"Content-Type": "application/json"}
        response = Request.post(url=url, headers=headers, data=json.dumps(req_data), timeout=20)
        code = response['code']
        callid = response['callid']

        return code, callid

    def upload_voice_file(self, path, file_name):
        """
        上传录音文件
        :param path: 要上传的文件路径
        :param file_name: 文件名
        :return:
        """
        url = self.host + "/ipcc/manager/file"

        with open(path, "rb") as f:
            files = f.read()

        file_size = len(files)

        req_data = {
            'appId': self.appid,
            'file': files,
            'filename': file_name
        }

        headers = {
            "Content-Type": "multipart/form-data",
            "Content-Length": file_size
        }
        response = Request.post(url=url, headers=headers, data=req_data, timeout=20)
        code = response['code']
        file_info = response.get("fileInfo")

        return code, file_info


