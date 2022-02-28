from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget


options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.instagram.com//")

WebDriverWait(chrome,10).until(EC.presence_of_all_elements_located((By.NAME,'username')))
username = chrome.find_element_by_name('username')
password = chrome.find_element_by_name('password')
username.send_keys("tsai_peng_peng")
password.send_keys("tsaipengpeng890811")

WebDriverWait(chrome,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')))
login_click = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_click.click()

WebDriverWait(chrome,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
store_click = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
store_click.click()

WebDriverWait(chrome,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
search = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
keyword = "#cat"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
WebDriverWait(chrome,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'FFVAD')))
images = chrome.find_elements_by_class_name('FFVAD')


#path = os.path.join(keyword)
#os.mkdir(path)

#count = 0 
for image in images:
    #save_as = os.path.join(path,keyword + str(count) + '.jpg')
    
    print(image.get_attribute("src"))
    #wget.download(image.get_attribute("src"),save_as)
    #count += 1