import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request


driver=webdriver.Chrome()
driver.get('https://upmusics.com/category/single-tracks/')

time.sleep(2)


lnks=driver.find_elements(By.TAG_NAME,"audio")
for lnk in lnks:
    print(lnk.get_attribute("src"))

    p=lnk.get_attribute("src").rfind("/")
    filename= lnk.get_attribute("src")[p+1:]
    #print (filename)
    urllib.request.urlretrieve(lnk.get_attribute("src"),filename)    
    break
    #if '.mp3'  in str(lnk.get_attribute("href")):
    #    print(lnk.get_attribute("href"))
