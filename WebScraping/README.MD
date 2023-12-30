# WEB SCRAPING
----
Web scraping is an automatic method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a database so that it can be used in various applications. There are many different ways to perform web scraping to obtain data from websites.

![img](https://github.com/RAJGUPTA28/QuickNLP-TextInspect/blob/main/WebScraping/download.png)

# Web Scraping Libraries & Tools
---
- Beautiful Soup.
- Requests.
- Scrapy.
- Selenium.
- Playwright.
- Lxml.
- Urllib3.
- MechanicalSoup.

# Beautiful Soup
(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

``` 
python -m pip install beautifulsoup4
```
Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping

``` from bs4 import BeautifulSoup ```


# Steps
1) Identify the target website
2) Collect URLs of the target pages
3) Make a request to these URLs to get the HTML of the page
4) Use locators to find the information in the HTML
5) Save the data in a JSON or CSV file or some other structured format
