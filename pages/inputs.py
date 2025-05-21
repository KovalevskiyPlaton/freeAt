from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
class Inputs:
    def __init__(self, browser):
        self.browser = browser
    def open_input(self,path):
        self.browser.get(path)

    def test_send_keys(self):
        
        driver = self.browser
        driver.find_element(By.XPATH, "//input[@class='form-control input-lg']").send_keys('basic text')

    def test_copy_paste(self, browser,value):
        driver = browser

        el=driver.find_element(By.XPATH, "//input[@class='form-control input-lg']")
        el.send_keys(value)

        action_chains=webdriver.ActionChains(driver)

        action_chains.key_down(Keys.CONTROL).send_keys('a').perform()
        action_chains.key_down(Keys.CONTROL).send_keys('c').perform()
        time.sleep(2)
        el.clear()
        el.click()
        time.sleep(2)
        pass
        action_chains.key_down(Keys.CONTROL).send_keys('v').perform()
        time.sleep(7)

    def test_input_mask(self, browser):   #тест на ввод симвлов в инпут №телефона
        driver = browser
        el= driver.find_element(By.XPATH, "//input[@name='phone']")
        value = '1234567899'
        for c in value:
            el.send_keys(c)
            time.sleep(0.1)
        el_end=driver.find_element(By.XPATH, "//form[@class='form-test']//input[@class='btn btn-primary']")
        time.sleep(2)
        el_end.click()
