from selenium import webdriver
from strategies import TwitterScraper, FacebookScraper, InstagramScraper
import configparser

# Scraper Login

class Scraper:
    def __init__(self, scraper):
        self.scraper = scraper

    def login(self, username, password):
        self.scraper.login(username, password)
    
    def scrap_posts(self):
        try:
            return self.scraper.scrap_posts()
        except Exception as e:
            print(e)

    def scrap(self):
        try:
            return self.scraper.scrap()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    url_test = "https://www.facebook.com/luciano.rocchetta"

    # Testing

    print("Testing running!")

    # Config
    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['credentials']['face_email']
    password = config['credentials']['face_password']

    # Define strategy
    app = Scraper(FacebookScraper(driver=driver, url=url_test))
    app.login(username=username, password=password)
    
    profile_data_result = app.scrap()
    posts = app.scrap_posts()
    
    print(profile_data_result)
    print(f"Posts: {posts}")
