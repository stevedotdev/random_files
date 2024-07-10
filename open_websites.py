import os
import subprocess
import sys
import time

# Function to install packages
def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except:
        return False

# Install necessary packages
if install('selenium') and install('webdriver-manager'):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
else:
    exit()

# Set up Chrome options
chrome_options = Options()

# Ensure compatibility with the default Chrome browser
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Set up the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# URL list of the websites to be opened
website_urls = [
    'http://example.com',
    'http://spork.org',
    'http://example.net',
    
]

try:
    # Open the first URL
    driver.get(website_urls[0])

    # Open the rest of the URLs in new tabs
    for url in website_urls[1:]:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(url)

    # Keeps the browser open
    input("Press Enter to close the browser...")

finally:
    driver.quit()