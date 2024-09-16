from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from .inteface import SocialMediaInterface

class TwitterScraper(SocialMediaInterface):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self, username, password):
        try:
            self.driver.get("https://twitter.com/login")
            time.sleep(3)
            username_input = self.driver.find_element_by_name("text")
            username_input.send_keys(username)
            username_input.send_keys(Keys.RETURN)
            time.sleep(3)
            password_input = self.driver.find_element_by_name("password")
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            time.sleep(5)
            print("Logged in to Twitter!")
        except Exception as e:
            print(f"Twitter login error: {e}")

    def scrap(self):
        try:
            self.driver.get(self.url)
            time.sleep(3)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            profile_name = soup.find("div", {"data-testid": "UserName"}).get_text() if soup.find("div", {"data-testid": "UserName"}) else None
            bio = soup.find("div", {"data-testid": "UserDescription"}).get_text() if soup.find("div", {"data-testid": "UserDescription"}) else None
            followers = soup.find("a", {"href": f"{url}/followers"}).get_text() if soup.find("a", {"href": f"{url}/followers"}) else None
            return {"name": profile_name, "bio": bio, "followers": followers}
        except Exception as e:
            print(f"Twitter scraping error: {e}")