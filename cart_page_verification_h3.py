from time import sleep

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

driver.find_element(By.ID, "nav-cart").click()
expected_text = "Your Amazon Cart is empty"
actual_result = driver.find_element(By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty").text

assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"

sleep(4)

# close the driver when done
driver.quit()