# 验证码处理工具
from PIL import Image
import pytesseract


def solve_captcha(image_path):
    return pytesseract.image_to_string(Image.open(image_path))
