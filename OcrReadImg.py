# from PIL import Image
# import pytesseract
import base64
import ddddocr
# from io import BytesIO
# from PIL import ImageOps


# 设置 Tesseract OCR 引擎的路径（根据你的安装路径修改）
# pytesseract.pytesseract.tesseract_cmd = r'D:\\Tesseract-OCR\\tesseract.exe'
# def recognize_captcha(image_path):
#     # 解码 base64 字符串
#     image_data = base64.b64decode(image_path)
#     # 使用 BytesIO 将字节流转换为文件对象
#     image_file = BytesIO(image_data)
#     # 打开验证码图片
#     captcha_image = Image.open(image_file).convert('RGB')
#     # 使用 Tesseract 进行 OCR 识别
#     # captcha_image = captcha_image.convert('L')  # 转为灰度图
#     captcha_image = ImageOps.grayscale(captcha_image)
#     captcha_image = captcha_image.point(lambda p: p > 235 and 255)
#     custom_config = r'--oem 3 --psm 9'
#     captcha_text = pytesseract.image_to_string(captcha_image,config=custom_config)
#     captcha_image.show()
#     text = captcha_text.strip().replace(" ","")
#     print(text)
def recognize_captcha(image_path):
    ocr = ddddocr.DdddOcr()
    image_data = base64.b64decode(image_path)
    res = ocr.classification(image_data)
    print(res)
    return res

# 调用验证码识别函数
# recognize_captcha(
#      "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")

