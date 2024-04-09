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
        #self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def lazy_loading(self, wait_time=2):
        current_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                WebDriverWait(self.driver, wait_time).until(
                    lambda driver: driver.execute_script
                                   ("return window.innerHeight + document.body.scrollHeight") != current_height)
                current_height = self.driver.execute_script("return window.innerHeight + document.body.scrollHeight")
            except TimeoutException:
                break

        return self.driver

    def define_urls(self):
        product_section = self.section
        url_pg_1 = f"https://www.amazon.com.au/gp/bestsellers/{product_section}/ref=zg_bs_pg_1_{product_section}?ie=UTF8&pg=1"
        url_pg_2 = f"https://www.amazon.com.au/gp/bestsellers/{product_section}/ref=zg_bs_pg_2_{product_section}?ie=UTF8&pg=2"
        return url_pg_1, url_pg_2

    def links_ranks(self):
        links = []
        ranks = []

        content = self.driver.page_source
        homepage_soup = BeautifulSoup(content, "html.parser")

        all_products = homepage_soup.find("div", attrs={"class": "p13n-desktop-grid"})

        if all_products is not None:
            for product_section in all_products.find_all("div", attrs={"id": "gridItemRoot"}):
                for link in product_section.find_all("a", {"tabindex": "-1"}):
                    if link["href"].startswith("https:"):
                        links.append(link["href"])
                    else:
                        links.append("https://www.amazon.com" + link["href"])
                rank = product_section.find("span", {"class": "zg-bdg-text"})
                ranks.append(rank.text)

        return links, ranks

    def content(self, url):
        self.driver.get(url)
        page_content = self.driver.page_source
        page_content_soup = BeautifulSoup(page_content, 'html.parser')
        return page_content_soup


def product_name(soup):
    try:
        name = soup.find('span', attrs={'id': "productTitle"}).text.strip()
    except:
        name = "Could Not Find a Name"
    return name


amazon_test = Amazon("computers")
urls = amazon_test.define_urls()
product_links = []
product_ranks = []
names = []

for page_url in urls:
    amazon_test.driver.get(page_url)
    amazon_test.lazy_loading()
    plinks, pranks = amazon_test.links_ranks()
    product_links.extend(plinks)
    product_ranks.extend(pranks)

for product in product_links:
    product_soup = amazon_test.content(product)
    the_name_of_the_product = product_name(product_soup)
    print(the_name_of_the_product)
    names.extend(the_name_of_the_product)

print(product_links)
print(product_ranks)
print(names)
