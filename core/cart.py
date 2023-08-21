# 购物车操作
from config import settings
from core.login import session


def add_to_cart(product_id):
    response = session.post(settings.PRODUCT_URL, data={"product_id": product_id})
    return response.status_code == 200
