from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Selenium website
driver.get("https://www.selenium.dev/")
driver.maximize_window()
time.sleep(3)

# Click Downloads using LINK TEXT
driver.find_element(By.LINK_TEXT, "Downloads").click()
time.sleep(3)

# Click Other Languages Exist using PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Other Languages").click()
time.sleep(3)

# Click Register Now using PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()
time.sleep(3)

# Fetch page title
print(driver.title)

driver.quit()