from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Facebook
driver.get("https://www.facebook.com")

driver.maximize_window()
time.sleep(3)

# Enter Email
driver.find_element(By.NAME, "email").send_keys("your_email")

# Enter Password
driver.find_element(By.NAME, "pass").send_keys("your_password")

time.sleep(5)

driver.quit()