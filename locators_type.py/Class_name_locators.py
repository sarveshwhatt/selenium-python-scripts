# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.myntra.com")

# search_box = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
# search_box.send_keys("shoes")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

login_button = driver.find_element(By.CLASS_NAME, "login-button")
login_button.click()