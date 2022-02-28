from pydoc import html
import time
from xml.dom.minidom import Document
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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

time.sleep(3)
chrome.get("https://www.instagram.com/bbcnews/")
#取得貼文連結
n_scroll = 5
post_url = []
for i in range(n_scroll):
    scroll = 'window.scrollTo(0,document.body.scrollHeight);'#javascript
    chrome.execute_script(scroll)
    html = chrome.page_source
    soup = Soup(html,'lxml')#beautful soup 2lxml解析器
    
    # 尋找所有的貼文連結
    for elem in soup.select('article div div div div a'):
        # 如果新獲得的貼文連結不在列表裡，則加入
        if elem['href'] not in post_url:
            post_url.append(elem['href'])
    time.sleep(2) # 等待網頁加載

# 總共加載的貼文連結數
print("總共取得 " + str(len(post_url)) + " 篇貼文連結")

    
