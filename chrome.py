from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the Chrome WebDriver executable
# webdriver_path = 'C:/path/to/chromedriver.exe'
# Create a new instance of ChromeDriver
driver = webdriver.Chrome()

# 1. Go to "https://amazon.in"
driver.get('https://www.amazon.in')

# 2. Search for "Wrist Watches"
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('Wrist Watches')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

# Apply filters
# Display: "Analogue"
display_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Analogue')]"))
)
display_filter.click()

# Brands Material: "Leather"
material_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Leather')]"))
)
material_filter.click()

# Brand: "Titan"
brand_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Titan')]"))
)
brand_filter.click()

# Discount: "25% Off or more"
discount_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '25% Off or more')]"))
)
discount_filter.click()

# 3. Get the Fifth Element from the search
fifth_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']:nth-child(5)"))
)
print(fifth_element.text)
