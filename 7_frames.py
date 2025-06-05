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
        driver.maximize_window()
        time.sleep(3)
        frame1 = driver.find_element(By.XPATH,"//*[@id='frame1']")
        driver.switch_to.frame(frame1)
        text1 = driver.find_element(By.ID,"sampleHeading").text
        print("Header is - "+text1)
        driver.switch_to.default_content()
        #driver.close()

launch1 = LaunchDemo()
launch1.LaunchBrowser("https://demoqa.com/frames")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
