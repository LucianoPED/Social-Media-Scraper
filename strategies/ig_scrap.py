from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from .inteface import SocialMediaInterface

class InstagramScraper(SocialMediaInterface):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self, username, password):
        try:
            self.driver.get("https://www.instagram.com/")

            time.sleep(3)

            username_input = self.driver.find_element_by_name("username")
            password_input = self.driver.find_element_by_name("password")

            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)

            time.sleep(5)

            print("Logged in to Instagram!")
        except Exception as e:
            print(f"Instagram login error: {e}")

    def scrap(self):
        try:
            self.driver.get(self.url)
            time.sleep(3)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            profile_name = soup.find("h1", {"id": "fb-timeline-cover-name"}).get_text() if soup.find("h1", {"id": "fb-timeline-cover-name"}) else None
            bio = soup.find("div", {"class": "biography"}).get_text() if soup.find("div", {"class": "biography"}) else None
            friends = soup.find("a", {"data-tab-key": "friends"}).get_text() if soup.find("a", {"data-tab-key": "friends"}) else None
            return {"name": profile_name, "bio": bio, "friends": friends}
        except Exception as e:
            print(f"Facebook scraping error: {e}")