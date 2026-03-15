# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get("https://www.facebook.com")

# forgot_link = driver.find_element(By.LINK_TEXT, "Forgotten password?")
# forgot_link.click()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

customer_service = driver.find_element(By.LINK_TEXT, "Customer Service")
customer_service.click()