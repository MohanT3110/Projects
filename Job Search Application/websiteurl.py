# import os.path

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time, re

def search_websites():

    #call Chrome Wedriver
    driver = webdriver.Chrome()

    # paste the Url
    url = "https://www.google.com/maps"

    # Open the URL in the browser
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # search the input
    search_input = driver.find_element(By.NAME, "q")

    # Input your search query
    search_query = "companies in hsr layout"
    search_input.send_keys(search_query)

    # Submit the search query (you can also use Keys.ENTER)
    search_input.send_keys(Keys.RETURN)

    # Wait for the search results to load
    driver.implicitly_wait(10)

    # Keep scrolling until the end of the list is reached
    divSideBar = driver.find_element(By.CSS_SELECTOR, f'div[aria-label^="Results for {search_query}"]')

    keepScrolling = True
    while keepScrolling:
        html = driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
        divSideBar.send_keys(Keys.ARROW_DOWN)
        if "You've reached the end of the list." in html:
            keepScrolling = False

    # Initialize a list to store website URLs
    website_urls = []

    # Find all the website links on the page
    website_links = driver.find_elements(By.XPATH, "//a[@href]")

    # Extract the website URLs from the links
    for link in website_links:
        website_url = link.get_attribute("href")
        if website_url.startswith("http"):
            website_urls.append(website_url)

    # Close the browser
    driver.quit()

    # Print the scraped website URLs
    website_urls = [url for url in website_urls if "google" not in url]
    website_urls = [url[:-1] for url in website_urls]
    return website_urls

# If this module is executed directly, call the search_websites function
if __name__ == "__main__":
    print(search_websites())




