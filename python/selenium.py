from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Use ChromeDriver or GeckoDriver)
driver = webdriver.Chrome()  
driver.get("https://www.linkedin.com/login")

# Log in
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("your_email")
password.send_keys("your_password")
password.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login

# Navigate to post/page
driver.get("https://www.linkedin.com/in/some-profile-or-post")

# Extract text
page_content = driver.page_source
print(page_content)

driver.quit()
