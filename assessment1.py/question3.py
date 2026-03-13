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

# Search for Mobiles (Using ID)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()

time.sleep(3)

# Click a mobile using PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung").click()

time.sleep(5)
driver.quit()