from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create Chrome options with incognito mode
options = webdriver.ChromeOptions()
options.add_argument('--incognito')

# create Chrome driver with options
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# navigate to a website in the incognito window
driver.get("https://www.amazon.com")

#CSS Selectors_hw

driver.find_element(By.CSS_SELECTOR, "div.a-section a.a-link-nav-icon i.a-icon")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "input#continue")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "div.a-row  a[href*='signin?']")

# close the driver when done
driver.quit()