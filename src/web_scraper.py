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
from datetime import date

class WebScraper:
    """
    WebScraper : The base class to the WebScraper application.

    Modules:
    --------
    __init__(self, URL, target) : initializes the WebScraper object
    """
    # URL = "https://realpython.github.io/fake-jobs/"
    def __init__(self, URL, driver=webdriver.Chrome()):
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
        # target = self.choose_option()
        self.URL = URL
        self.driver = driver
        self.open_url()

    def open_url(self):
        """
        Launches the driver, using the Chrome browser

        Parameters:
        -----------
        none
        """
        driver = self.driver
        driver.maximize_window()
        driver.get(self.URL)

    def choose_option(self):
        """
        allows the user to choose the content to scrape: text or image

        returns target(str)

        Parameters:
        -----------
        target : str
            this is the specification for what to scrape
            options include:
                - "img" : images
                - "txt" : text
                - "img_txt" : both images and text
        """
        valid = False
        while not valid:
            try:
                target = input('Choose the target data to scrape:\n"text" or "img"\n')
                if target.lower() == "text" or target.lower() == "img":
                    valid = True
                else:
                    raise ValueError
            except ValueError:
                print("Entry not valid.")
                print('Only enter "text" or "img"')

        return target


    def request_url(self):
        """
        sends a request to the URL, and captures the HTML content

        returns the get response

        Parameters:
        -----------
        none
        """
        response = requests.get(self.URL)

        return response
    
    def beautiful_soup_text(self, content):
        """
        Method that creates the Beautiful Soup object, from the content
        attribute of the response from a request.get() command. The response
        is parsed using the "html-parser" option from beautiful soup, 
        which is appropriate for HTML content

        returns the beautiful soup object

        Parameters:
        -----------
        content : bytes
            bytes object; derived from invoking the .content method on a URL
            response object
        """
        return BeautifulSoup(content, "html.parser")
    
    def create_new_log_text(self, title, content):
        """
        creates a new .csv file containing the contents of the scraped data

        Parameters:
        -----------
        content : str
            content of the HTML from the URL that was scraped
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        temp = current_directory.split("\\")
        print("This is temp: ", temp)
        del temp[-1]
        temp.append("scrapes")
        scrape_directory = "/".join(temp)
        # scrape_directory = scrape_directory.replace("/","\\")

        title_mod = title.replace(" ", "_")

        datetime_object_now = datetime.datetime.now()

        title_time_csv = title_mod + '_' + \
            datetime_object_now.strftime("%d-%b-%Y_H%HM%MS%S") + ".csv"

        print("This is title_time_csv: ", title_time_csv)

        with open(scrape_directory+'/'+title_time_csv, "a") as file:
            file.write(f"{title}\n")
            file.write(datetime_object_now.strftime("%d-%b-%Y_H%HM%MS%S") + "\n\n")
            file.write(str(content))

    def close_driver(self):
        self.driver.close()


        
URL = "https://realpython.github.io/fake-jobs/"
driver = webdriver.Chrome()
inst = WebScraper(URL = URL, driver = driver)

response = inst.request_url()
response_beautifulsoup_obj = inst.beautiful_soup_text(response.content)

title = inst.driver.title
content = response.content

inst.create_new_log_text(title, content)

