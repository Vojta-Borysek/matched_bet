from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options
import time
import concurrent.futures
import queue


class Betano:
    def scrape_page(self, url, result_queue):
        # Configure Chrome options for headless mode
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration to prevent some rendering issues

        # Initialize the WebDriver with the configured options
        # driver = webdriver.Chrome(options=chrome_options)

        firefox_options = FirefoxOptions()
        # Uncomment the line below if you want to run Firefox in headless mode
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--start-maximized")

        # Initialize the WebDriver with the configured options
        driver = webdriver.Firefox(options=firefox_options)

        # Open the web page
        driver.get(url)

        time.sleep(2)
        close = driver.find_element(By.XPATH, "//button[@class='sb-modal__close__btn uk-modal-close-default uk-icon uk-close']")
        driver.execute_script("arguments[0].click();", close)
        close.click()
        time.sleep(2)

        # Find the container for the events
        events_container = driver.find_element(By.CLASS_NAME, "events-list__grid__info__main__row")
        # events-list__grid
        # Find all the individual event <div> elements within the container
        event_divs = events_container.find_elements(By.CLASS_NAME, "table__markets__market")
        # events-list__grid__event

        # Loop through the found elements and extract the desired data
        # numb = 0
        team_odds_list_full = []
        for event_div in event_divs:
            team_odds_list = []
            # Extract date and time
            # numb += 1
            # datetime_div = event_div.find_element(By.CLASS_NAME, "events-list__grid__info__datetime")
            # date = datetime_div.find_element(By.XPATH, ".//span[1]").text
            # time = datetime_div.find_element(By.XPATH, ".//span[2]").text

            # Extract team names
            team_divs = event_div.find_elements(By.CLASS_NAME,
                                                "events-list__grid__info__main__participants__participant-name")
            team1 = team_divs[0].text
            team2 = team_divs[1].text

            odds_buttons = event_div.find_elements(By.CSS_SELECTOR, ".selections__selection__odd")
            odds = [button.text for button in odds_buttons[:3]]

            # Print the extracted data
            # print("Date:", date)
            # print("Time:", time)
            # print("Team 1:", team1)
            teams = team1 + ' - ' + team2
            # team_odds_list.append(team1)
            # result_queue.put(team1)
            # print("Team 2:", team2)
            # team_odds_list.append(team2)
            # result_queue.put(team2)
            # print(teams)
            # print(odds)
            # team_odds_list.append(odds)
            result_queue.put(teams)
            result_queue.put(odds)
            # print()
            team_odds_list_full.append(team_odds_list)

        # Close the WebDriver
        # print(numb)
        # print(team_odds_list_full)
        driver.quit()

        # result_queue.put(team_odds_list_full)
    # URLs to scrape

    result_queue = queue.Queue()

    # Scrape the pages concurrently
    def betano(self):
        # urls = GetBTURLS().getbturls()
        urls = ["https://www.betano.cz/sport/fotbal/souteze/ceska-republika/11338/",
                "https://www.betano.cz/sport/fotbal/souteze/liga-mistru/188566/",
                "https://www.betano.cz/sport/fotbal/souteze/evropska-konferencni-liga/189602/",
                "https://www.betano.cz/sport/fotbal/souteze/anglie/1/",
                "https://www.betano.cz/sport/fotbal/souteze/spanelsko/2/",
                "https://www.betano.cz/sport/fotbal/souteze/italie/87/",
                "https://www.betano.cz/sport/fotbal/souteze/nemecko/24/",
                "https://www.betano.cz/sport/fotbal/souteze/francie/23/",
                "https://www.betano.cz/sport/fotbal/souteze/portugalsko/11382/",
                "https://www.betano.cz/sport/fotbal/souteze/nizozemsko/11376/",
                "https://www.betano.cz/sport/fotbal/souteze/turecko/11384/",
                "https://www.betano.cz/sport/fotbal/souteze/evropska-liga/188567/",
                "https://www.betano.cz/sport/fotbal/souteze/albanie/11317/",
                "https://www.betano.cz/sport/fotbal/souteze/belgie/11324/",
                "https://www.betano.cz/sport/fotbal/souteze/bosna-a-hercegovina/11478/",
                "https://www.betano.cz/sport/fotbal/souteze/bulharsko/11328/",
                "https://www.betano.cz/sport/fotbal/souteze/chorvatsko/11334/",
                "https://www.betano.cz/sport/fotbal/souteze/dansko/11339/",
                "https://www.betano.cz/sport/fotbal/souteze/estonsko/11411/",
                "https://www.betano.cz/sport/fotbal/souteze/finsko/11355/",
                "https://www.betano.cz/sport/fotbal/souteze/gruzie/11436/",
                "https://www.betano.cz/sport/fotbal/souteze/irsko/11367/",
                "https://www.betano.cz/sport/fotbal/souteze/island/10008/",
                "https://www.betano.cz/sport/fotbal/souteze/izrael/11429/",
                "https://www.betano.cz/sport/fotbal/souteze/kypr/11336/",
                "https://www.betano.cz/sport/fotbal/souteze/madarsko/11363/",
                "https://www.betano.cz/sport/fotbal/souteze/malta/11491/",
                "https://www.betano.cz/sport/fotbal/souteze/moldavsko/11442/",
                "https://www.betano.cz/sport/fotbal/souteze/norsko/11378/",
                "https://www.betano.cz/sport/fotbal/souteze/polsko/11381/",
                "https://www.betano.cz/sport/fotbal/souteze/rakousko/11322/",
                "https://www.betano.cz/sport/fotbal/souteze/recko/90/",
                "https://www.betano.cz/sport/fotbal/souteze/rumunsko/11383/",
                "https://www.betano.cz/sport/fotbal/souteze/severni-irsko/11377/",
                "https://www.betano.cz/sport/fotbal/souteze/skotsko/91/",
                "https://www.betano.cz/sport/fotbal/souteze/slovensko/11392/",
                "https://www.betano.cz/sport/fotbal/souteze/slovinsko/11435/",
                "https://www.betano.cz/sport/fotbal/souteze/srbsko/11389/",
                "https://www.betano.cz/sport/fotbal/souteze/svedsko/11393/",
                "https://www.betano.cz/sport/fotbal/souteze/svycarsko/11394/",
                "https://www.betano.cz/sport/fotbal/souteze/ukrajina/11386/",
                "https://www.betano.cz/sport/fotbal/souteze/wales/11433/"]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for url in urls:
                futures.append(executor.submit(self.scrape_page, url, self.result_queue))

            # Wait for all threads to finish
            for future in concurrent.futures.as_completed(futures):
                pass

        # Collect the results from the queue
        all_results = []
        while not self.result_queue.empty():
            all_results.append(self.result_queue.get())

        print(all_results)
        return all_results
        # print(len(all_results))
