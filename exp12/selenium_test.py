# selenium_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
# network / cert relaxations helpful for local Docker tests
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--ignore-certificate-errors")
opts.add_argument("--allow-insecure-localhost")
opts.add_argument("--disable-web-security")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=opts
)

# Use host.docker.internal so the browser in the selenium container reaches your host-published app
driver.get("http://host.docker.internal:8000")

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "get-started"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("abc@gmail.com")
    driver.find_element(By.ID, "pwd").send_keys("password")
    driver.find_element(By.ID, "loginBtn").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dash")))
    print("✅ Login Successful")
except Exception as e:
    print("❌ Login Failed:", e)
finally:
    driver.quit()
