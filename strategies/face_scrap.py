from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from .inteface import SocialMediaInterface

class FacebookScraper(SocialMediaInterface):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def wait_for_elements(self, by_type, elements):
        for elem in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by_type, elem)))

    def login(self, username, password):
        try:
            self.driver.get("https://www.facebook.com/login")

            self.wait_for_elements(
                By.NAME,
                ["email", "pass"]
            )

            username_input = self.driver.find_element(By.NAME, "email")
            password_input = self.driver.find_element(By.NAME, "pass")

            print(username_input, password_input)

            username_input.send_keys(username)
            password_input.send_keys(password)

            password_input.send_keys(Keys.ENTER)

            print("Logged in to Facebook!")
        except Exception as e:
            print(f"Facebook login error: {e}")

    def scrap_posts(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id=":rbq:"]/div/div/span/div[1]/div'))
            )

            posts = self.driver.find_elements(By.XPATH, '//*[@id=":rbq:"]/div/div/span/div[1]/div')
            return posts

        except Exception as e:
            print(f"Error scraping posts: {e}")
            return None

    def scrap(self):
        try:
            print(self.url)
            self.driver.get(self.url)

            self.wait_for_elements(By.CLASS_NAME, ['html-h1'])

            soup = BeautifulSoup(self.driver.page_source, "html.parser")

            profile_name = soup.find("h1", class_='html-h1').get_text() if soup.find("h1", class_="html-h1") else None
            #bio = soup.find("div", {"class": "biography"}).get_text() if soup.find("div", {"class": "biography"}) else None
            #friends = soup.find("a", {"data-tab-key": "friends"}).get_text() if soup.find("a", {"data-tab-key": "friends"}) else None
            
            #return {"name": profile_name, "bio": bio, "friends": friends}
            return {"name": profile_name}
        except Exception as e:
            print(f"Facebook scraping error: {e}")