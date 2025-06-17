from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# For screenshot
import os
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver
CHROMEDRIVER_PATH = r"C:\\Users\\TamekaGrant\webDriverschromedriver.exe\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Set up Chrome options (optional)
options = Options()
options.add_argument("--start-maximized")

# Create driver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open Wikipedia
    driver.get("https://www.wikipedia.org")
    time.sleep(2)

    # Step 2: Validate Title
    title = driver.title
    if "Wikipedia" in title:
        print(f"✅ Title is correct: {title}")
    else:
        print(f"❌ Title is incorrect: {title}")

    # Step 3: Take Screenshot
    screenshot_path = os.path.join(os.getcwd(), "homepage.png")
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved to {screenshot_path}")

finally:
    # Step 4: Close the browser
    driver.quit()
