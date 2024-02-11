import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


class getSMURLS:
    def geturls(self):
        # Initialize the WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()  # You can use other drivers like Firefox, etc.

        # Load the URL
        url = "https://smarkets.com/sport/football"
        driver.get(url)

        time.sleep(4)

        # Find all the links with the specified class
        link_elements = driver.find_elements(By.CLASS_NAME, "header.topic-link.collapsed")

        # Extract the first seven links and store them in an array
        links_array = []
        for i, link_element in enumerate(link_elements):
            if i >= 7:  # Only extract the first seven links
                break
            link = link_element.get_attribute("href")
            links_array.append(link)

        excluded_urls = [
            "https://smarkets.com/watchlist",
            "https://smarkets.com/inplay",
            "https://smarkets.com/listing/sport/football?period=today",
            "https://smarkets.com/listing/sport/football?period=tomorrow",
            "https://smarkets.com/listing/sport/football/outright"
        ]

        valid_links = []

        # Loop through the first seven links and perform some actions
        for link in links_array:
            driver.get(link)
            time.sleep(2)
            link_e = driver.find_elements(By.CLASS_NAME, "header.listing-link.collapsed")
            # Add a delay to see the action
            for link_ee in link_e:
                li = link_ee.get_attribute("href")
                if li not in excluded_urls:
                    valid_links.append(li)
            # Go back to the original page
            driver.back()
            time.sleep(2)

        # Close the WebDriver
        driver.quit()
        # Close the web driver
        # original_stdout = sys.stdout  # Save a reference to the original standard output
        # with open('o.txt', 'w', encoding="utf-8") as f:
            # sys.stdout = f  # Change the standard output to the file we created.
            # print(valid_links)
        # sys.stdout = original_stdout
        print('Got ' + str(len(valid_links)) + ' links from SM')
        return valid_links
        # print(len(valid_links))
