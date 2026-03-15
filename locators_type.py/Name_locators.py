# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.youtube.com")

# search_box = driver.find_element(By.NAME, "search_query")
# search_box.send_keys("melody hits")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

search_box = driver.find_element(By.NAME, "field-keywords")
search_box.send_keys("mobile phone")