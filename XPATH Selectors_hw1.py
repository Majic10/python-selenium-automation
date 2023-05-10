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


driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
driver.find_element(By.XPATH, "//label[@class='a-form-label']")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "continue")
driver.find_element(By.XPATH ,"//div[@id='legalTextRow']//a[contains(@href, 'condition_of_use')]")
driver.find_element(By.XPATH ,"//div[@id='legalTextRow']//a[contains(@href, 'privacy_notice')]")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")
driver.find_element(By.ID, "createAccountSubmit")

# close the driver when done
driver.quit()
