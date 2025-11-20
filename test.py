from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # or Firefox()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("DevOps Automation")
search_box.submit()

print("Title:", driver.title)
driver.quit()