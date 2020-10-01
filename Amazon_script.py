from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/ayantknv/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html/')

input_field = driver.find_element(By.ID, 'helpsearch')
input_field.send_keys('cancel order')

search_icon = driver.find_element(By.XPATH, "//input[@name='help_keywords']")
search_icon.submit()

result = driver.find_element(By.XPATH, "//b['cancel order']")
assert result.text == 'cancel order'
