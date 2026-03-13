from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Amazon
driver.get("https://www.amazon.in")

driver.maximize_window()
time.sleep(3)

# Click Update Location
driver.find_element(By.ID, "nav-global-location-popover-link").click()

time.sleep(5)

driver.quit()