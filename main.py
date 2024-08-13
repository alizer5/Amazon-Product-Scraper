
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#driver.get("https://www.amazon.in/s?k=laptops&crid=1E005D9ZPU4IR&sprefix=lapt%2Caps%2C691&ref=nb_sb_noss_2")
# driver.get('https://www.amazon.com.au/s?k=laptop&crid=2C5YCBM5PBKFG&sprefix=laptop%2Caps%2C389&ref=nb_sb_noss_1')
#elem = driver.find_elements(By.CLASS_NAME, "sg-col-inner")
# # print(len(elem))
# for el in elem:
#   print(el.text)
file=0
query='laptops'
for i in range(1,20):
    driver.get(f'url')
    elem=driver.find_elements(By.CLASS_NAME,"puis-card-container")

    for el in elem:
        d=el.get_attribute('outerHTML')
        with open(f'data/{query}_{file}.html','w',encoding='utf-8') as f:
            f.write(d)
            file+=1
            time.sleep(2)



driver.close()


