# coding=utf8
import requests
import json


# post请求
def post(url, data, header):
    try:
        json_data = json.dumps(data)
        headers = {"Content-Type": "application/json"}
        if header:
            headers.update(header)
        response = requests.post(url, data=json_data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"POST请求发生错误：{e}")


# get请求
def get(url, data, header):
    try:
        headers = {}
        if header:
            headers.update(header)
        response = requests.get(url, params=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f" GET请求发生错误：{e}")
