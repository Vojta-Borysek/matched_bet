from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import concurrent.futures


class BetanoScraper:
    global_results = []

    def __init__(self, urls):
        self.urls = urls

    def scrape_url(self, url):
        firefox_options = FirefoxOptions()
        # Uncomment the line below if you want to run Firefox in headless mode
        firefox_options.add_argument("--headless")

        # Initialize the WebDriver with the configured options
        driver = webdriver.Firefox(options=firefox_options)

        # Open the web page
        driver.get(url)

        time.sleep(2)

        # Close any modal if present
        try:
            close = driver.find_element(By.XPATH, "//button[@class='sb-modal__close__btn uk-modal-close-default uk-icon uk-close']")
            driver.execute_script("arguments[0].click();", close)
            time.sleep(1)
        except:
            pass

        # events_container = driver.find_elements(By.CLASS_NAME, "events-list__grid__info__main__row")
        # event_divs = driver.find_elements(By.CLASS_NAME, "table__markets__market")

        # Use XPath to locate the first element
        elements = driver.find_elements(By.XPATH, '//div[@class="tw-flex tw-w-full tw-flex-col ml:tw-flex-row"]')

        odds = []
        for element1 in elements:
            # Use XPath to locate the second element within the first element
            element2 = element1.find_element(By.XPATH, './/div[@class="tw-flex"]')

            # Do something with the second element, for example, print its text
            # match print(element2.text)
            element2 = element2.text.replace("\n", " - ")
            # odds.append(element2)

            # Use XPath to locate the third element within the first element
            element3 = element1.find_element(By.XPATH, './/div[@class="selections"]')

            # Do something with the third element, for example, print its text
            # print(element3.text)
            element3 = element3.text.replace("1\n", "")
            element3 = element3.replace("\n0\n", ", ")
            element3 = element3.replace("\n2\n", ", ")
            element3 = element3.split(", ")
            # odds.append([element3])

            self.global_results.append(element2)
            self.global_results.append(element3)
        time.sleep(1)
        # Close the WebDriver after processing each URL
        driver.quit()

    def scrape_all_urls(self):
        # num_threads = min(len(self.urls), 4)  # Adjust the number of threads based on the number of URLs and your system capabilities

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the scraping tasks and store the Future objects
            futures = [executor.submit(self.scrape_url, url) for url in self.urls]

            # Gather the results as they complete
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                self.global_results.append(result)

        cleaned_data = [item for item in self.global_results if item is not None]
        return cleaned_data
