import time

from selenium import webdriver
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
        parent_window = driver.current_window_handle
        print(parent_window)
        driver.find_element(By.XPATH, "//span[normalize-space()='Where2Go']").click()
        time.sleep(5)
        windowHandles = driver.window_handles
        print(len(windowHandles))
        for handle in windowHandles:
            if handle != parent_window:
                driver.switch_to.window(handle)

        driver.find_element(By.XPATH, "//a[@href='/tripideas/beach-destinations']//h3[@class='DestinationCard__CardTitle-sc-1czmno9-1 gMbbQW']").click()
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parent_window)

        driver.close()

window1 = demoWindow()
window1.autowindow()