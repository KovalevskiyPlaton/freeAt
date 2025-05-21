from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.common.by import By

class TestInput:
    def test_send_keys(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://automationexercise.com/products')  #"//input[@class='form-control input-lg']"
        driver.find_element(By.XPATH, "//input[@class='form-control input-lg']").send_keys('basic text')

        time.sleep(7)

    def test_clear(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://automationexercise.com/products')  #"//input[@class='form-control input-lg']"
        el=driver.find_element(By.XPATH, "//input[@class='form-control input-lg']")
        el.send_keys('basic text')

        el.clear()
        time.sleep(7)

    def test_copy_paste(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://automationexercise.com/products')  #"//input[@class='form-control input-lg']"
        el=driver.find_element(By.XPATH, "//input[@class='form-control input-lg']")
        el.send_keys('basic text')

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


    def test_input_mask(self, set_up_browser):   #тест на ввод симвлов в инпут №телефона
        driver = set_up_browser
        driver.get('https://daruse.ru/proverka-vvoda-nomera-telefona-cherez-jquery?ysclid=matdztx5ts392432979')  #"//input[@class='form-control input-lg']"
        #el=driver.find_element(By.XPATH, "//input[@name='phone']").send_keys('1234567899') #в случае если символы очень быстро вводятся можно ипользовать цикл ниже и введные данные  отображаются некорректно
        el= driver.find_element(By.XPATH, "//input[@name='phone']")
        value = '1234567899'
        for c in value:
            el.send_keys(c)
            time.sleep(0.1)
        el_end=driver.find_element(By.XPATH, "//form[@class='form-test']//input[@class='btn btn-primary']")
        el_end.click()

    def test_input_filter(self, set_up_browser):   #тест на ввод только кирилицы
        driver = set_up_browser
        driver.get('https://ktjnwv.csb.app/')  #"//input[@class='form-control input-lg']"

        pass
        el_enter = driver.find_element(By.PARTIAL_LINK_TEXT,'Yes, proceed to')
        el_enter.click()
        time.sleep(3)
        el= driver.find_element(By.XPATH, "//input[@id='test-input']").send_keys('123ffззбрllиыы')
        time.sleep(7)
        pass

#

    def test_input_tag(self, set_up_browser):   #тест на ввод только кирилицы
        driver = set_up_browser
        driver.get('https://www.geeksforgeeks.org/how-to-create-tags-input-box-in-html-css-and-javascript/')  #"//input[@class='form-control input-lg']"



        el= driver.find_element(By.XPATH, "//input[@id='input-tag']").send_keys('123ffззбрllиыы')
        time.sleep(10)

        pass







