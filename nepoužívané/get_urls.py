from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import sys
import time


class GetBTURLS:
    def getbturls(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration to prevent some rendering issues

        # Initialize the WebDriver with the configured options
        driver = webdriver.Chrome(options=chrome_options)

        # Load the URL
        url = "https://www.betano.cz/sport/fotbal/"
        driver.get(url)

        time.sleep(2)

        # Wait for the clickable elements to load
        wait = WebDriverWait(driver, 10)
        clickable_elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tw-w-icon-xxxs.tw-h-icon-xxxs.tw-rotate-180"))
        )

        # Scroll the page to make the elements clickable
        for element in clickable_elements:
            actions = ActionChains(driver)
            try:
                actions.move_to_element(element).perform()
                element.click()
            except:
                pass


        elements = driver.find_elements(By.TAG_NAME, "a")

        urls = []

        # Filter and extract the URLs based on class names that start with 'tw-text-xs'
        for element in elements:
            class_names = element.get_attribute("class").split()
            for class_name in class_names:
                if class_name.startswith("tw-text-xs"):
                    href = element.get_attribute("href")
                    # print(href)
                    urls.append(href)
                    break  # No need to check other class names for this element

        # Close the web driver
        original_stdout = sys.stdout  # Save a reference to the original standard output
        with open('o.txt', 'w', encoding="utf-8") as f:
            sys.stdout = f  # Change the standard output to the file we created.
            print(urls)
        sys.stdout = original_stdout  # Reset the standard output to its original value
        print('Got ' + str(len(urls)) + ' links from Betano')
        driver.quit()
        return urls
