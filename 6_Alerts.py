# PIP - Package Installer for Python.
# PIP install selenium
# selenium.dev - official webste -> downloads - python
# pip install webdriver-manager - install web drver manage
# can install from terminal also. same command.
# vertual - for that project, global - for all the projects.
# selector hub - to inspect objects
# DemoQA.com
import time

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
        time.sleep(2)

        driver.find_element(By.ID,"confirmButton").click()
        alert1 = driver.switch_to.alert
        time.sleep(2)
        alert1.accept()
        #use below code for 4th alert in DemoQA site
        #alert1.send_keys("Hellow")
        #alert1.dismiss()
        time.sleep(2)
        driver.close()

launch1 = LaunchDemo()
launch1.LaunchBrowser("https://demoqa.com/alerts")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
