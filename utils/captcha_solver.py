# 验证码处理工具
from datetime import time

from PIL import Image
import pytesseract
import requests


# 使用pytesseract解决简单的图像验证码
def solve_image_captcha(image_path):
    return pytesseract.image_to_string(Image.open(image_path))


# 使用2Captcha解决复杂的验证码，如reCAPTCHA
def solve_recaptcha(site_key, page_url, api_key):
    service_url = "http://2captcha.com/in.php"
    params = {
        "key": api_key,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": page_url,
        "json": 1
    }
    response = requests.get(service_url, params=params).json()
    request_result = response.get("request")

    if response.get("status") == 1:
        # 等待2Captcha解决验证码
        for _ in range(15):  # 等待最多30秒
            solution = requests.get(
                f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_result}&json=1").json()
            if solution.get("status") == 1:
                return solution.get("request")
            time.sleep(2)
    return None
