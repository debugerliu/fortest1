import requests
import json


def test_login():
    url = "https://api-hometest.xzm.cn/upm/user/login"

    payload = json.dumps({
        "loginName": "testA123@bank888",
        "password": "testA123456",
        "platform": "VUE"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
