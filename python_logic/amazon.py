

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

class Amazon:
    def __init__(self, section):
        self.section = section  
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    
    def lazy_loading(self, wait_time=2):
        current_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            try:
                WebDriverWait(self.driver, wait_time).until(
                    lambda driver: driver.execute_script("return window.innerHeight + document.body.scrollHeight") != current_height
                )
                current_height = self.driver.execute_script("return window.innerHeight + document.body.scrollHeight")
            except TimeoutException:
                break

        return self.driver

    def links_ranks(self):
        links = []
        ranks = []
    
        content = self.driver.page_source
        homepage_soup = BeautifulSoup(content, "html.parser")
    
        all_products = homepage_soup.find("div", attrs={"class": "p13n-desktop-grid"})
    
        for product_section in all_products.find_all("div", attrs={"id": "gridItemRoot"}):
            for link in product_section.find_all("a", {"tabindex": "-1"}):
                if link["href"].startswith("https:"):
                    links.append(link["href"])
                else:
                    links.append("https://www.amazon.com" + link["href"])
            rank = product_section.find("span", {"class": "zg-bdg-text"})
            ranks.append(rank.text)
        
        return links, ranks
    
