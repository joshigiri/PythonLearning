import time

from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains    # this has to be imported.
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class demoWindow():
    def autowindow(self):
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
        time.sleep(2)

        # for right clicking
        action_chains = ActionChains(driver)
        #this will not click on any web element right clicks top left corner
        action_chains.context_click().perform()

        elem1 = driver.find_element(By.XPATH,"//span[normalize-space()='From']")
        action_chains.context_click(elem1).perform()
        time.sleep(3)

        #moves mouse to that position
        action_chains.move_to_element(elem1).perform()

        driver.close()

window1 = demoWindow()
window1.autowindow()