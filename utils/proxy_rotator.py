import random


class ProxyRotator:
    """代理轮换工具"""

    def __init__(self, proxies_list, max_failures=3):
        self.proxies_list = proxies_list
        self.max_failures = max_failures
        self.failures = {proxy: 0 for proxy in proxies_list}

    def get_proxy(self):
        """获取一个代理，并确保其失败次数未超过最大值"""
        valid_proxies = [p for p in self.proxies_list if self.failures[p] < self.max_failures]
        if not valid_proxies:
            # 重置失败次数并重新获取代理列表
            self.reset_failures()
            valid_proxies = self.proxies_list
        return random.choice(valid_proxies)

    def report_failure(self, proxy):
        """报告代理失败"""
        self.failures[proxy] += 1

    def reset_failures(self):
        """重置所有代理的失败次数"""
        self.failures = {proxy: 0 for proxy in self.proxies_list}


# 加载代理列表
def load_proxies_from_file(file_path="config/proxies.txt"):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]
