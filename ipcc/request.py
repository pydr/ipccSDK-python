
import requests


class Request(object):

    @staticmethod
    def post(*args, **kwargs):
        global result
        try:
            print("requesting-> ", kwargs.get("url"))
            response = requests.post(*args, **kwargs)
            result = response.json()

        except ConnectionError:
            result = {"code": "200000", "callId": ""}

        return result



