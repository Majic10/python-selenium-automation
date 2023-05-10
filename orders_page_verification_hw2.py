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

driver.find_element(By.ID, "nav-orders").click()
expected_text = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"

sleep(4)

# close the driver when done
driver.quit()