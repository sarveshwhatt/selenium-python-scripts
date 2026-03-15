# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get("https://www.wikipedia.org")

# heading = driver.find_element(By.TAG_NAME, "h1")

# print(heading.text)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

button = driver.find_element(By.TAG_NAME, "button")

button.click()