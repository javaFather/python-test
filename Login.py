import json

import requests
import base64
import re
# pip install Pillow
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import importlib
import Config as config
from OcrReadImg import recognize_captcha

# 验证码
def base64_to_image(base64_string):
    # 解码 base64 字符串
    # image_data = base64.b64decode(base64_string)
    result = recognize_captcha(base64_string)
    # 使用 BytesIO 将字节流转换为文件对象
    # image_file = BytesIO(image_data)
    # 使用 Pillow 打开图像文件对象
    # image = Image.open(image_file)
    # plt.figure(figsize=(2, 2))
    # 显示图像
    # plt.imshow(image)
    # plt.show(block=False)
    # plt.pause(2)
    return result


# 更新cookie
def write_cookie(cookie_value):
    with open("Config.py", "r", encoding="utf-8") as file:
        content = file.read()
        # 替换 cookie
        content = re.sub(r'^\s*cookie\s*=\s*".*"', f'cookie = "{cookie_value}"', content, flags=re.MULTILINE)
        # 写入新值
        with open("Config.py", "w", encoding="utf-8") as file:
            file.write(content)
            file.close()
    # 刷新配置
    importlib.reload(config)


def login_with_captcha(username, password):
    # 登录url
    login_url = "http://stg1-iops.daikuan.qihoo.net/iops/user/login"
    # 创建一个 Session 对象，用于保持 cookie
    session = requests.Session()
    # 从响应中提取验证码图片的 URL
    captcha_url = "http://stg1-iops.daikuan.qihoo.net/iops/user/login/captchaV2"
    captcha_response = session.get(captcha_url)
    image64 = captcha_response.json()["data"]["imageBytes"]
    token = captcha_response.json()["data"]["token"]
    # 展示验证码
    # base64_to_image(image64)
    # 手动输入验证码
    # captcha_input = input("请输入验证码：")
    captcha_input = base64_to_image(image64)
    # 构造登录请求的数据，包括用户名、密码和验证码
    data = {"currentLogin": "account", "username": username, "password": password, "captcha": captcha_input,
            "token": token, "bagClass": 1}

    # 发送包含验证码的登录请求
    headers = {"Content-Type": "application/json"}
    data_json = json.dumps(data)
    response = session.post(login_url, data=data_json, headers=headers)
    # 检查登录是否成功（可根据实际情况修改判断条件）
    if "S".__eq__(json.loads(response.text)["flag"]):

        print("登录成功")
        # all_cookies = session.cookies.get_dict()
        # for cookie in all_cookies:
        #     print(f"Cookie: {cookie.name}={cookie.value}")
        # token = response.json().get("token")
        # print(token)
        # todo 设置cookie
        write_cookie("aaa")
    else:
        print("登录失败")
