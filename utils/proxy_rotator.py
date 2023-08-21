# 代理轮换工具
import random


def get_random_proxy():
    with open("config/proxies.txt", "r") as f:
        proxies = f.readlines()
    return random.choice(proxies).strip()
