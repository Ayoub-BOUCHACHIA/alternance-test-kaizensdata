from http.cookies import SimpleCookie
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import random
import json



def crawl_page(url,scroll_count=40):
    """
    request and crawl the page from the `url` parameter, and scroll down the page in order to load more data.
    the parameter `scroll_count` specifies how many times the page should be scrolled.
    """

    # get twitter cookie from the json file cookie_twitter.json
    
    with open ('media/test_main/cookie_twitter.json', "r") as f:    
        # Reading from file
        twitter_COOKIE = json.loads(f.read())

    # Set chrome webdriver options
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    # initialize chrome webdriver
    driver = webdriver.Firefox(executable_path="media/test_main/geckodriver")

    
    driver.get(url)
    # Parse cookies from string format to Python Dict
    cookie = SimpleCookie()
    cookie.load(twitter_COOKIE)
    for key, morsel in cookie.items():
        driver.add_cookie(
            {"name":key,"value":morsel.value}
        )

    # In order to apply the new cookies settings, we need to request the page again and reload the browser for the cookies settings to take effect.
    driver.get(url)
    driver.refresh()
    for i in range(1,scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down the page
        time.sleep(random.randint(3,5)) # using random to avoid being blocked
        
    # Saving the html source code
    html_source = driver.page_source
    
    return html_source