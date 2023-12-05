from bs4 import BeautifulSoup
from selenium.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException

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
            this is the target URL, in http form.
        target : str
            this is the specification for what to scrape
            options include:
                - "img" : images
                - "txt" : text
                - "img_txt" : both images and text
        """
        self.URL = URL
        self.target = target
