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
        print (driver.title)        # prints the title
        driver.find_element(By.LINK_TEXT,"Contact").click()
        #driver.find_element(By.ID, "name2").send_keys("Prasad1")

        if driver.find_element(By.NAME,"name2").is_displayed():
             driver.find_element(By.XPATH,"//*[@name='name2']").send_keys("Girish1")

        # find elements
        eles = driver.find_elements(By.CLASS_NAME,"form-control")
        eles[2].send_keys("9886182100")
        time.sleep(3)

        # for all the elements
        for i in eles:
            i.clear()
            i.send_keys("Demo")
            print ("Attribute name: "+i.get_attribute("placeholder"))
        time.sleep(3)



launch1 = LaunchDemo()
launch1.LaunchBrowser("https://www.dharwadhubballitutor.com/")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
