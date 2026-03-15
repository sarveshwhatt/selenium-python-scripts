# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get("https://www.facebook.com")

# email = driver.find_element(By.XPATH, "//input[@id='email']")
# email.send_keys("test@gmail.com")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_box.send_keys("laptop")