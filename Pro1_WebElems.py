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
        #driver.maximize_window()
        driver.fullscreen_window()
        #driver.minimize_window()
        #driver.forward()
        #driver.refresh()
        driver.find_element(By.LINK_TEXT,"Contact").click()
        #driver.find_element(By.ID, "name2").send_keys("Prasad1")
        driver.find_element(By.XPATH,"//*[@name='name2']").send_keys("Girish1")
        time.sleep(3)
        #driver.close()

        #sel1 = Select("")
        #sel1.select_by_index()

launch1 = LaunchDemo()
launch1.LaunchBrowser("https://www.dharwadhubballitutor.com/")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
