import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# set up Chrome options to use incognito mode and maximize window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--start-maximized')

# create a new Chrome instance with the options
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# navigate to the website
driver.get("https://www.amazon.com")

# perform a search for a product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Pen")
search_box.submit()
time.sleep(4)
# select the desired product and add it to cart
product = driver.find_element(By.CSS_SELECTOR, "img.s-image[src='https://m.media-amazon.com/images/I/81HTgYFwyfL._AC_UL400_.jpg']")
time.sleep(4)
driver.execute_script("arguments[0].scrollIntoView();", product)
product.click()
time.sleep(4)
add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart_btn.click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"a[href='/cart?ref_=sw_gtc']").click()

expected_text = "Shopping Cart"
actual_result = driver.find_element(By.CSS_SELECTOR, "div.a-row h1").text
assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"

time.sleep(10)
driver.quit()