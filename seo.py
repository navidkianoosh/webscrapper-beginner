import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.google.com')

time.sleep(2)

sb=driver.find_element('name','q')

sb.send_keys('آزمايش نيشابور')
sb.submit()

time.sleep(3)

lnks=driver.find_elements(By.TAG_NAME,"a")
for lnk in lnks:
    print(lnk.get_attribute("href"))
    if 'attarlab.ir'  in str(lnk.get_attribute("href")):
        lnk.click()

time.sleep(3)
driver.close()
driver.quit()

