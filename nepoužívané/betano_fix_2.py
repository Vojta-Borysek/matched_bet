from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import concurrent.futures

url = "https://www.betano.cz/sport/fotbal/ceska-republika/1-liga/16952/"
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

# Use XPath to locate the first element
elements = driver.find_elements(By.XPATH, '//div[@class="tw-flex tw-w-full tw-flex-col ml:tw-flex-row"]')

odds = []
for element1 in elements:
    # match = []
    # Use XPath to locate the second element within the first element
    element2 = element1.find_element(By.XPATH,'.//div[@class="tw-flex"]')

    # Do something with the second element, for example, print its text
    #match print(element2.text)
    element2 = element2.text.replace("\n", " - ")
    odds.append(element2)

    # Use XPath to locate the third element within the first element
    element3 = element1.find_element(By.XPATH, './/div[@class="selections"]')

    # Do something with the third element, for example, print its text
    # print(element3.text)
    element3 = element3.text.replace("1\n", "")
    element3 = element3.replace("\n0\n", ", ")
    element3 = element3.replace("\n2\n", ", ")
    odds.append([element3])
    # odds.append(match)
print(odds)
driver.quit()
