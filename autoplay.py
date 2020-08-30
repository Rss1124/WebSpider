from lib2to3.pgen2 import driver

import selenium as selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
class ifPlay():
    def __call__(self,driver):
        if driver.find_element_by_xpath("//*[@id='bofqi']"):
            return True
        else:
            return False
def play():
    if(WebDriverWait(driver,10,0.5).until(ifPlay())):
        driver.find_element_by_xpath("//*[@id='bofqi']").click()
        print("播放数+1")
        driver.refresh()
        time.sleep(20)
    else:
        print("播放失败")
        play()
driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/video/BV1YJ411e7E5")
while(1):
    play()
    time.sleep(300)
    