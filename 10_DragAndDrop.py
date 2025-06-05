import time

# https://pypi.org/project/webdriver-manager/

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

        action_chain = ActionChains(driver)
        source = driver.find_element(By.XPATH,"//div[@id='draggable']")
        target = driver.find_element(By.XPATH,"//div[@id='droppable']")

        #this will drag and drop from src to target
        #action_chain.drag_and_drop(source, target).perform()
        action_chain.click_and_hold(source).move_to_element(target).release().perform()
        #try the slider option also in demoQA

        #ctrl + a option
        action_chain.key_down(Keys.CONTROL).send_keys("a").key_down(Keys.CONTROL).perform()
        time.sleep(3)
        #slider operations below code.
        # action_chain.drag_and_drop_by_offset(source,100,0).perform()
        # action_chain.click_and_hold(source).move_by_offset(100,0).perform()

        driver.close()

launch1 = LaunchDemo()
launch1.LaunchBrowser("https://demoqa.com/droppable")