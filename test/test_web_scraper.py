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

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        print("Setting up TestWebScraper")        
    
    def tearDown(self):
        print("Tearing down TestWebScraper")