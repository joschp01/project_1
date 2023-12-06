# Notes: Beautiful Soup

Refer to the following for more details:

- [Beautiful Soup Quick Guide](https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_quick_guide.htm)

- [Beautiful Soup: Build a Web Scraper with Python](https://realpython.com/beautiful-soup-web-scraper-python/)

To start programming the web scraper tool, we will first need to consider what such a tool is needed for. To web scrape, the tool would first need to access a website. This can be achieved by opening a browser driver, and requesting data from a URL. The data received can vary in structure and data, since every webpage is created for a specific purpose which might have a use for a certain feature, but not others, and vice versa.

## What is Web Scraping?

To scrape a webpage, means the same as grabbing/extracting data from it. Developers are then able to collect and analyze the data. Web Scraping can be automated, and the retrieved data analyzed in an organized way.

## Language used: Python

Python offers a few perks when used for web scraping:

1. **Ease of Use**: Python's format, which allows for omitting curly braces "{ } " or semi-colons allows for better readability

2. **Huge Library Support**: Python supports different purposes with its vast libraries for web scraping, and can then use other libraries for visualizing/analyzing the data visually, and using machine learning.

3. **Easily Explicable Syntax**: Along with ease of use by being robust in formatting, the language itself is very expressive of the intended functionality.

4. **Dynamically-typed language**: Python is dynamically typed, meaning that a variable takes on the type of the value it is assigned. This saves a lot of time and makes work faster.

5. **Huge Community**: Python has a large user base, and can therefore be a great resource for any blocks in the workflow.


## (Optional) Creating a virtual environment

In order to isolate the project to its own environment, we will create a virtual environment. To install the package, we will use pip. (prior to installing, check first that pip is not installed by executing the following command in git bash. You can get git bash for your system by just simply googling how to do so:)

```bash
pip --version
# returns the pip version installed
```

To install pip, execute the following code:

```bash
 $sudo apt-get install python-pip
```

To create a virtual environment, we need to install virtual environment. Execute the following command to install virtual environment:

```bash
pip install virtualenv
```

Once installed, we can create the virtual environment, and activate it with the following commands:

```bash
python -m venv venv
```
* Note: Summary of the command - "using the venv command, create a virtual environment "venv""

Now, in order to freely install what is needed for our project, we have to activate the virtual environment first. After navigating to the directory directly above the "venv" directory, execute the following command:

```bash
source venv/Scripts/activate
```

There should be an indicator above the command lines which looks like the virtual environment folder's name, within parenthesis. In our case, the command lines will have something like this: "(venv)." With the virtual environment activated, we can execute "pip install [package]" and it won't affect our entire system.

## Library: Beautiful Soup

Summary: Beautiful Soup is a python package, which have methods that can help in parsing through data, and organizing/formatting the gathered data by fixing bad HTML and presents the data in an XML structure.

```
"Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML/XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree" 
```
[Source](https://pypi.org/project/beautifulsoup4/)

To start using Beautiful Soup, first we must install the package that contains it. Execute the following command:

```bash
pip install beautifulsoup4
# installs the beautifulsoup4 package
# name of package is "bs4" when importing
```

Once it is installed, all you need to do to begin using beautiful soup is add the following line in the Python module:

```python
from bs4 import BeautifulSoup
```

