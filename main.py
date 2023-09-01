import logging

from config import settings
from core.cart import add_to_cart
from core.checkout import checkout
from core.login import login
from core.stock import monitor_stock
from utils.proxy_rotator import ProxyRotator, load_proxies_from_file
from utils.user_agents import AdvancedUserAgentRotator

# 初始化日志
logging.basicConfig(level=logging.INFO)

# 初始化代理轮换器
proxies_list = load_proxies_from_file()
proxy_rotator = ProxyRotator(proxies_list)

# 初始化User-Agent轮换器
user_agent_rotator = AdvancedUserAgentRotator()


def main():
    # 设置代理和User-Agent
    proxy = proxy_rotator.get_proxy()
    user_agent = user_agent_rotator.get_random_user_agent()
    headers = {"User-Agent": user_agent}

    # 1. 登录
    if not login(settings.LOGIN_URL, settings.USERNAME, settings.PASSWORD, proxy, headers):
        logging.error("Login failed.")
        return

    # 2. 监控商品库存
    if not monitor_stock(settings.PRODUCT_URL, proxy, headers):
        logging.error("Product is still out of stock after monitoring.")
        return

    # 3. 添加商品到购物车
    if not add_to_cart(settings.CART_URL, settings.PRODUCT_URL, proxy, headers):
        logging.error("Failed to add product to cart.")
        return

    # 4. 结账
    if not checkout(settings.ADDRESS, settings.CONTACT, proxy, headers):
        logging.error("Failed to checkout.")
        return

    logging.info("Successfully purchased the product!")


if __name__ == "__main__":
    main()
