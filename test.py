import base64

import pytest
import requests


def getBase64Code(codePath):
    '''python生成图片的base64编码'''
    with open(codePath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s


def test_all_request():

    for i in range(1,20):
        path = f'img/1/{i}.jpg'
        code = getBase64Code(path)

        data = {"image_base64": f"{code}"}
        res = requests.post('http://127.0.0.1:8080/post',json=data)
        print(res.text)


