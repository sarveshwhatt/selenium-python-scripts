# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get("https://www.facebook.com")

# forgot_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten")
# forgot_link.click()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

service_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Customer")
service_link.click()