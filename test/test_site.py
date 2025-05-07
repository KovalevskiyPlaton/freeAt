from pages.homepage import HomePage
from pages.product import ProductPage
import time


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page=ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
    #browser.get('https://demoblaze.com/index.html')

    #galaxy_s6=browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]') #=> it`s working
    #galaxy_s6 =browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    #galaxy_s6.click()
    #title = browser.find_element(By.CSS_SELECTOR, 'h2')
    #assert title.text == 'Samsung galaxy s6'

def test_two_monitor(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_products_count(2)


    #browser.get('https://demoblaze.com/index.html')
    #check_2Monit=browser.find_element(By.LINK_TEXT, 'Monitors')
    #check_2Monit=browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    #check_2Monit.click()
    #time.sleep(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, '.h-100') #monitors == monitors
    #monitors=browser.find_elements(By.XPATH, '''//div[@class='col-lg-4 col-md-6 mb-4']''')
    #assert len(monitors)==2

#Проект с автотестами => нужны знания по ООП