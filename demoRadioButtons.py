import time

from  selenium.webdriver.support.select import Select

# https://pypi.org/project/webdriver-manager/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager



class LaunchDemo():
    def LaunchBrowser(self, strURL):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get(strURL)
        # print TITTLE
        print (driver.title)

        #click Create new account
        driver.find_element(By.LINK_TEXT,"Create new account").click()
        time.sleep(2)

        print(driver.find_element(By.XPATH, "//input[@value='1']").is_selected())
        driver.find_element(By.XPATH,"//input[@value='1']").click()
        print(driver.find_element(By.XPATH,"//input[@value='1']").is_selected())



launch1 = LaunchDemo()
launch1.LaunchBrowser("https://www.facebook.com/")
