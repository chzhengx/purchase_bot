from core import login, cart, checkout
from core.cart import add_to_cart

if __name__ == "__main__":
    if login():
        if add_to_cart("new_iphone_id"):
            checkout()
