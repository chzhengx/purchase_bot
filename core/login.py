import requests
from utils.captcha_solver import solve_recaptcha, solve_image_captcha


def login(login_url, username, password, proxy, headers):
    """
    登录函数
    :param login_url: 登录页面的URL
    :param username: 用户名
    :param password: 密码
    :param proxy: 使用的代理
    :param headers: 请求头，包括User-Agent
    :return: 登录是否成功
    """
    session = requests.Session()

    # 获取登录页面，可能需要处理验证码或其他安全检查
    response = session.get(login_url, headers=headers, proxies=proxy)
    response.raise_for_status()

    # 如果页面有验证码，这里处理它
    # 这只是一个示例，实际的实现可能会根据验证码的类型和位置有所不同
    if "captcha" in response.text:
        captcha_solution = solve_image_captcha(response.content)
        # 或者，如果是reCAPTCHA：
        # site_key = "YOUR_SITE_KEY"
        # captcha_solution = solve_recaptcha(site_key, login_url, "YOUR_2CAPTCHA_API_KEY")

    # 提交登录表单
    login_data = {
        "username": username,
        "password": password,
        "captcha": captcha_solution  # 如果有验证码
    }
    response = session.post(login_url, data=login_data, headers=headers, proxies=proxy)
    response.raise_for_status()

    # 检查是否登录成功
    # 这只是一个示例，实际的检查可能会根据返回的内容有所不同
    if "login successful" in response.text:
        return True
    else:
        return False
