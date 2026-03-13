from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.wikipedia.org")


driver.refresh()


print("Wikipedia Title:", driver.title)


driver.get("https://www.amazon.com")


print("Amazon Title:", driver.title)


driver.back()


driver.quit()