import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class demoAuto():
    def autoSuggest(self):
        SearchFrom = "Beng"
        FromCity = "Bengaluru"
        SearchTo = "Mum"
        ToCity = "Mumbai"
        date = "Jun 21 2025"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='From']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys(SearchFrom)
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[text()='" + FromCity + "']").click()

        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='To']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys(SearchTo)
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[text()='" + ToCity + "']").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//div[contains(@aria-label,'" + date + "')]").click()
        time.sleep(5)

        driver.close()


auto = demoAuto()
auto.autoSuggest()
