import requests 
import time
import datetime
from sleeptime import seconds_until_end_of_today
from sendmsg import sendmsg
from check import check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import itertools
import pandas as pd
import pywintypes
from win10toast import ToastNotifier
import os
toast = ToastNotifier()
toast.show_toast("File Organizer", "The Process has been started.",duration=30)
os.chdir(r'C:\Users\Bilal Sheikh\Desktop\codeproject\birthday project')
while 1==1:    
    #current date
    today=datetime.date.today().day
    #internet connection
    while True:
        try:
            requests.get('https://www.google.com/').status_code
            print("connection established")
            break
        except:
            time.sleep(5)
            pass
    #Running just one time after each five minutes
    while (datetime.date.today().day == today):
        time.sleep(300)
    #Real program
    #finding is there anyones birthday today
    df = pd.read_csv(r'C:\Users\Bilal Sheikh\Desktop\codeproject\birthday project\datasample.csv', encoding= 'unicode_escape')
    for i in df.index:
        if check((df.loc[i].at["Day"].item()),(df.loc[i].at["Month"].item()),(datetime.date.today().day),(datetime.date.today().month))==1:
            sendmsg(df.loc[i].at["Name"],str(df.loc[i].at["Mobile Number"]))
        else: 
            pass