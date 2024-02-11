from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class betano_urls_all:
    def __int__(self):
        pass

    def get_all_urls(self):
        firefox_options = FirefoxOptions()
        # Uncomment the line below if you want to run Firefox in headless mode
        firefox_options.add_argument("--headless")

        # Initialize the WebDriver with the configured options
        driver = webdriver.Firefox(options=firefox_options)
        # Open the webpage
        url = "https://www.betano.cz/sport/fotbal/ceska-republika/1-liga/16952/"
        driver.get(url)

        time.sleep(2)

        # Close any modal if present
        try:
            close = driver.find_element(By.XPATH, "//button[@class='sb-modal__close__btn uk-modal-close-default uk-icon uk-close']")
            driver.execute_script("arguments[0].click();", close)
            time.sleep(1)
        except:
            pass

        try:
            roll = driver.find_element(By.XPATH, '//div[@class="tw-relative tw-max-w-full tw-cursor-pointer"]')
            driver.execute_script("arguments[0].click();", roll)
            time.sleep(1)
        except:
            pass

        # Find the element using XPath
        xpath = '//a[contains(@class, "tw-flex")]/div[@class="tw-text-n-28-cloud-burst tw-text-[12px] tw-leading-s tw-truncate"]'
        elements = driver.find_elements(By.XPATH, xpath)

        urls = []
        # Now you can interact with the element as needed, for example, printing its text
        for element in elements:
            # Extract the href attribute from the <a> element
            href = element.find_element(By.XPATH, './..').get_attribute('href')
            # Check if the href contains "vylepsene-kurzy"
            if "vylepsene-kurzy" in href:
                break
            urls.append(href)
            if len(urls) == 1500:
                break
        # Close the webdriver
        driver.quit()
        print('Got ' + str(len(urls)) + ' links from Betano')
        print(urls)
        return urls
