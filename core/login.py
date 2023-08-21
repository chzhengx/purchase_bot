# 登录相关功能
import requests
from config import settings

session = requests.Session()


def login():
    response = session.post(settings.LOGIN_URL, data={"username": settings.USERNAME, "password": settings.PASSWORD})
    return response.status_code == 200
