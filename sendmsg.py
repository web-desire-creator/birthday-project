from selenium.common.exceptions import NoSuchElementException 
import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from finderror import check_exists_by_xpath
def sendmsg(name, number):
    while 1==1:
        msg= 'Happy Birthday '+name+'. May God shower you with blessings today and always.'
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=C:\\Users\\Bilal Sheikh\\Desktop\\codeproject\\birthday project\\user-data")
        chrome_options.add_argument('--profile-directory=Default')
        driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\Bilal Sheikh\\Desktop\\codeproject\\birthday project\\chromedriver.exe")
        wait = WebDriverWait(driver, 1)
        print("Chrome opened successfully!")
        #internet connection
        while True:
            try:
                requests.get('https://www.google.com/').status_code
                print("connection established")
                break
            except:
                time.sleep(5)
                pass
        Web_whatsapp = 'https://web.whatsapp.com/send?phone='+number[0:5]+number[6:]  # To go to whatsapp web
        driver.get(Web_whatsapp)
        time.sleep(25)
    #Checking mobile connection
            
        try:
            inp_xpath = '//div[@role="textbox"][@class="_13NKt copyable-text selectable-text"][@contenteditable="true"][@data-tab="9"][@dir="ltr"][@spellcheck="false"]'
            #<div role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="9" dir="ltr" spellcheck="false"></div>
            input_box = driver.find_element_by_xpath(inp_xpath)
            print("Accessing Whatsapp web")
            time.sleep(2)
            input_box.send_keys(msg + Keys.ENTER)
            time.sleep(2)
            driver.close()
            break
        except NoSuchElementException:
            print("Mobile is still not connected")
            driver.close()
