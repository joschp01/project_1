from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import requests

class WebScraper:
    """
    WebScraper : The base class to the WebScraper application.

    Modules:
    --------
    __init__(self, URL, target) : initializes the WebScraper object
    """
    def __init__(self, URL, target):
        """
        Initializes the WebScraper object

        Parameters:
        -----------
        URL : str
            this is the target URL.
        target : str
            this is the specification for what to scrape
            options include:
                - "img" : images
                - "txt" : text
                - "img_txt" : both images and text
        """
        self.URL = URL
        self.target = target

    def open_url(self):
        """
        Launches the driver, using the Chrome browser

        Parameters:
        -----------
        none
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.URL)

    def request_URL(self):
        """
        sends a request to the URL, and captures the HTML content

        returns the URL HTML content

        Parameters:
        -----------
        none
        """
        page = requests.get(self.URL)

        return page.text

inst = WebScraper("https://realpython.github.io/fake-jobs/", "")
# inst.open_url()
URL_HTML = inst.request_URL()
print(type(URL_HTML))

