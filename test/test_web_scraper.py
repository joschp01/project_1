import unittest

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import requests
import os
import datetime

from src.web_scraper import WebScraper
# from ..src.web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    URL = "https://realpython.github.io/fake-jobs/"
    def setUp(self):
        print("Setting up TestWebScraper")
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.scraper = WebScraper(driver = self.driver)
    
    def tearDown(self):
        print("Tearing down TestWebScraper")
        self.driver.close()

    def test_01_save_scrape_data(self):
        """
        tests that the module is able to save HTML data to a .csv or .json file

        user story:
        -----------
        "As a user, I want the ability to save the scraped data into a file (such as CSV or JSON) for future reference or analysis."
        """
        scraper = self.scraper
        content = (requests.get(self.URL)).content

        current_directory = os.path.dirname(os.path.abspath(__file__))
        temp = current_directory.split("\\")
        del temp[-1]
        temp.append("scrapes")
        scrape_directory = "\\".join(temp)

        print("This is self.driver.title: ", self.driver.title)
        file_name = self.driver.title.replace(" ", "_") + "_" + str(datetime.date.today())

        file_directory = os.path.join(scrape_directory, file_name)
        print("This is file_directory: ", file_directory)
        with open(file_directory, 'r') as file:
            self.assertEqual(content, file)