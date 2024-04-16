from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class Amazon:
    """
    A class representing an Amazon web scraper.

    Attributes:
        section (str): The section of Amazon website to scrape.
        options (webdriver.ChromeOptions): Chrome options for the web driver.
        driver (webdriver.Chrome): The Chrome web driver.

    Methods:
        __init__(self, section): Initializes a new instance of the Amazon class.
        lazy_loading(self, wait_time=2): Performs lazy loading of the web page.
        define_urls(self): Defines the URLs for the specified section.
        links_ranks(self): Retrieves the links and ranks of the products.
        content(self, url): Retrieves the content of a specific URL.
    """

    def __init__(self, section):
        """
        Initializes a new instance of the Amazon class.

        Args:
            section (str): The section of Amazon website to scrape.
        """
        self.section = section
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=self.options
        )

    def lazy_loading(self, wait_time=2):
        """
        Performs lazy loading of the web page.

        Args:
            wait_time (int): The time to wait for the page to load (default is 2 seconds).

        Returns:
            webdriver.Chrome: The Chrome web driver.
        """
        current_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            try:
                WebDriverWait(self.driver, wait_time).until(
                    lambda driver: driver.execute_script(
                        "return window.innerHeight + document.body.scrollHeight"
                    )
                    != current_height
                )
                current_height = self.driver.execute_script(
                    "return window.innerHeight + document.body.scrollHeight"
                )
            except TimeoutException:
                break

        return self.driver

    def define_urls(self):
        """
        Defines the URLs for the specified section.

        Returns:
            tuple: A tuple containing the URLs for page 1 and page 2.
        """
        product_section = self.section
        url_pg_1 = f"https://www.amazon.com.au/gp/bestsellers/{product_section}/ref=zg_bs_pg_1_{product_section}?ie=UTF8&pg=1"
        url_pg_2 = f"https://www.amazon.com.au/gp/bestsellers/{product_section}/ref=zg_bs_pg_2_{product_section}?ie=UTF8&pg=2"
        return url_pg_1, url_pg_2

    def links_ranks(self):
        """
        Retrieves the links and ranks of the products.

        Returns:
            tuple: A tuple containing the links and ranks of the products.
        """
        links = []
        ranks = []

        content = self.driver.page_source
        homepage_soup = BeautifulSoup(content, "html.parser")

        all_products = homepage_soup.find("div", attrs={"class": "p13n-desktop-grid"})

        if all_products is not None:
            for product_section in all_products.find_all(
                "div", attrs={"id": "gridItemRoot"}
            ):
                for link in product_section.find_all("a", {"tabindex": "-1"}):
                    if link["href"].startswith("https:"):
                        links.append(link["href"])
                    else:
                        links.append("https://www.amazon.com.au" + link["href"])
                rank = product_section.find("span", {"class": "zg-bdg-text"})
                ranks.append(rank.text)

        return links, ranks

    def content(self, url):
        """
        Retrieves the content of a specific URL.

        Args:
            url (str): The URL to retrieve the content from.

        Returns:
            BeautifulSoup: The parsed HTML content of the page.
        """
        self.driver.get(url)
        self.lazy_loading()
        page_content = self.driver.page_source
        page_content_soup = BeautifulSoup(page_content, "html.parser")
        return page_content_soup


def valid_sections():
    sections = [
        "amazon-devices",
        "audible",
        "automotive",
        "baby-products",
        "beauty",
        "books",
        "fashion",
        "computers",
        "electronics",
        "garden",
        "gift-cards",
        "health",
        "home",
        "home-improvement",
        "kitchen",
        "lighting",
        "movies-and-tv",
        "music",
        "musical-instruments",
        "grocery",
        "pet-supplies",
        "software",
        "sporting-goods",
        "office-products",
        "toys",
        "videogames",
    ]
    return sections


def product_name(soup):
    """
    Extracts the name of a product from the given BeautifulSoup object.

    Parameters:
    - soup: A BeautifulSoup object representing the HTML content of a webpage.

    Returns:
    - name: The name of the product as a string. If the name cannot be found, it returns "Could Not Find a Name".
    """
    try:
        name = soup.find("span", attrs={"id": "productTitle"}).text.strip()
    except:
        name = "Could Not Find a Name"
    return name


def product_price(soup):
    """
    Extracts the price of a product from the given BeautifulSoup object.

    Parameters:
    - soup: BeautifulSoup object representing the HTML content of a webpage.

    Returns:
    - price: The price of the product as a string. If the price cannot be found, returns "Could Not Find a Price".
    """
    try:
        price_area = soup.find("span", attrs={"class": "a-price"}).text.strip()
        price = price_area.find("span", attrs={"class": "a-offscreen"}).text.strip()
    except:
        price = "Could Not Find a Price"
    return price


def product_rating(soup):
    """
    Extracts the rating of a product from the given BeautifulSoup object.

    Parameters:
    - soup: A BeautifulSoup object representing the HTML content of a webpage.

    Returns:
    - rating: The rating of the product as a string. If the rating cannot be found, returns "Could Not Find a Rating".
    """
    try:
        rating = soup.find(
            "span", attrs={"data-hook": "rating-out-of-text"}
        ).text.strip()
    except:
        rating = "Could Not Find a Rating"
    return rating


def product_photo(soup):
    try:
        photo = soup.find("img", attrs={"id": "landingImage"})
        photo_url = photo["src"]
    except:
        photo_url = "Could Not Find a Photo"
    return photo_url
