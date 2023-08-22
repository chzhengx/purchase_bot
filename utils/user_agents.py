import random
import requests


class AdvancedUserAgentRotator:
    """User-Agent生成工具"""

    def __init__(self):
        self.user_agents_db = self.load_from_file("config/user_agents.txt")
        self.devices = ["Windows", "Macintosh", "Linux", "iPhone", "Android"]
        self.browsers = ["Chrome", "Firefox", "Safari", "Edge"]
        self.versions = ["68.0", "69.0", "70.0", "71.0"]  # 示例版本号

    @staticmethod
    def load_from_file(file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

    @staticmethod
    def fetch_from_online_api(api_url="https://www.someapi.com/useragents"):
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return []

    def generate_user_agent(self):
        device = random.choice(self.devices)
        browser = random.choice(self.browsers)
        version = random.choice(self.versions)
        return f"Mozilla/5.0 ({device}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"

    def get_random_user_agent(self):
        # 优先从数据库中获取
        if self.user_agents_db:
            return random.choice(self.user_agents_db)
        # 其次尝试在线API
        online_user_agents = self.fetch_from_online_api()
        if online_user_agents:
            return random.choice(online_user_agents)
        # 最后，动态生成
        return self.generate_user_agent()
