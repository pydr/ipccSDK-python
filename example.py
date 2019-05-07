import threading

import colorama

from ipcc.client import Client
from server.server import httpd

appid = "turing-test"  # 申请的appid
host = "http://172.17.0.10"  # 分配的ipcc server
number = "9512345" # 数字线路标识


client = Client(host, appid)

t = threading.Thread(target=httpd.serve_forever)
t.start()


def demo():

    # 发起通知型呼叫
    code, callid = client.notify(number, "13800138000", "我的梦想是世界和平")
    if code != "000000":
        print(colorama.Back.RED + "ERROR", "呼叫失败")

    # 发起呼叫
    # code, callid = client.out_call("9512345", "13800138000", data="data")
    # if code != "000000":
    #     print(colorama.Back.RED + "ERROR", "呼叫失败")


if __name__ == '__main__':
    colorama.init(autoreset=True)
    demo()

