import os
import subprocess
import sys
import argparse

# URL list of the websites to be opened
URLS = [
    'http://example.com',
    'http://spork.org',
    'http://example.net',
    'http://travelassist.com',
    'http://fogcam.org',
    'http://milk.com',
    'https://www.oldest.org/technology/oldest-websites-still-editing/',
    'http://aliweb.com',
    'http://info.cern.ch',
    'https://www.washingtonian.com/2024/07/03/meet-the-smithsonian-bird-detectives-saving-lives/',
    'http://cfg.com',
    'http://tic.com',
    'http://vortex.com',
    'http://itcorp.com',
]

# Function to install packages
def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except:
        return False

# Install necessary packages
if (install('selenium') and install('webdriver-manager')):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.edge.options import Options as EdgeOptions
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
else:
    exit()

# Function to get the driver based on the browser choice
def get_driver(browser):
    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser.lower() == "firefox":
        firefox_options = FirefoxOptions()
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    elif browser.lower() == "edge":
        edge_options = EdgeOptions()
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    elif browser.lower() == "safari":
        return webdriver.Safari()
    else:
        raise ValueError("Unsupported browser. Please choose 'Chrome', 'Firefox', or 'Edge'.")

# Set up argument parser
parser = argparse.ArgumentParser(description='Open multiple websites in specified browser.')
parser.add_argument('-b', '--browser', required=True, help="Browser to use (Chrome, Firefox, Edge)")
parser.add_argument('-n', '--num_windows', type=int, required=True, help="Number of windows to open (max 5)")

args = parser.parse_args()

# Ensure the number of windows is within the limit
if args.num_windows < 1 or args.num_windows > 5:
    print("Error: Number of windows must be between 1 and 5.")
    sys.exit(1)

# Function to split URLs into chunks
def split_urls(urls, num_windows):
    avg = len(urls) // num_windows
    chunks = []
    for i in range(num_windows):
        start = i * avg
        if i == num_windows - 1:  # last chunk, include the rest
            chunks.append(urls[start:])
        else:
            chunks.append(urls[start:start + avg])
    return chunks

# Split the URLs among the number of browser instances
url_chunks = split_urls(URLS, args.num_windows)

# List to store driver instances
drivers = []

try:
    # Open the URLs in separate browser instances
    for chunk in url_chunks:
        driver = get_driver(args.browser)
        for url in chunk:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
        drivers.append(driver)

    # Keeps the browsers open
    input("Press Enter to close the browsers...")
finally:
    # Quit all drivers
    for driver in drivers:
        driver.quit()