from selenium.webdriver.chrome import webdriver
from time import sleep
driver=webdriver.WebDriver()
driver.maximize_window()
driver.get("https://www.baidu.com")
print(driver.title)
sleep(2)
driver.quit()