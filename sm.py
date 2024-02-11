from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from get_url_sm import getSMURLS


class Smarkets:
    # Function to scrape data from a URL
    all_data = []

    def scrape_data(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        time.sleep(4)

        elements = driver.find_elements(By.CLASS_NAME, "item-tile")

        for e in elements:
            odds = []
            teams = e.find_elements(By.CLASS_NAME, "team-name")
            team_names = ' - '.join([team.text for team in teams])

            bids = e.find_elements(By.CLASS_NAME, "bid")

            for i in range(len(bids)):
                try:
                    bid_price = bids[i].find_element(By.CLASS_NAME, "price").text
                    odds.append(bid_price)
                except:
                    bid_price = 1000
                    odds.append(bid_price)
                finally:
                    continue

            self.all_data.append(team_names)
            self.all_data.append(odds)

        driver.quit()

    def smarkets(self):
        threads = []
        # List of URLs to scrape
        urls = getSMURLS().geturls()

        # Create and start threads for each URL
        for url in urls:
            thread = threading.Thread(target=self.scrape_data, args=(url,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # print(self.all_data)
        return self.all_data
        # print(len(self.all_data))
