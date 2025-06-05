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
from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager



class LaunchDemo():
    def LaunchBrowser(self, strURL):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get(strURL)
        time.sleep(3)
        #driver.close()

launch1 = LaunchDemo()
launch1.LaunchBrowser("https://www.google.co.in/")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
