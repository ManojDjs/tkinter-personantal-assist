from selenium import webdriver
import time
from pymongo import MongoClient
def login():
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    #options.add_argument('headless')
    #options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=options, executable_path=r'D:\software\chromedriver.exe')
    browser.get("https://facebook.com")
    login=browser.find_element_by_id("email")
    passw=browser.find_element_by_id("pass")
    time.sleep(1)
    login.send_keys("07404089651") #enter email in ""
    passw.send_keys("Aisha@1866")   #enter password in ""
    browser.find_element_by_id("u_0_b").click()
    browser.get('https://www.facebook.com/djsmanoj.prince')

    post_box = browser.find_element_by_xpath('//div[@class="m9osqain a5q79mjw"]')
    post_box.click()
    post=browser.find_element_by_xpath('//div[@class="ll8tlv6m"]')

    post.send_keys("heya i  posted using python script.")
    time.sleep(2)
    post_it = browser.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
    post_it.click()
    print("Posted...")

login()