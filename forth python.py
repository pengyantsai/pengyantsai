from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome()
driver.get('https://tsj.tw/')
blow = driver.find_element_by_id('click')
blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
items = []
items.append( driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i'))
items.append( driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
items.append( driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))

prices = []
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))

actions = ActionChains(driver)


for i in range(100):
    actions.click(blow)
    actions.perform()
    count = int(blow_count.text.replace("您目前擁有","").replace("技術點",""))
    for j in range(3):
        price = int(prices[j].text.replace("技術點",""))
        if price <= count:
            #upgread_actions = ActionChains(driver)
            actions.move_to_element(items[j])
            actions.click()
            actions.perform()
            break



