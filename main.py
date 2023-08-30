from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
chrome_driver_path = "/Users/Development/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome()
i=91
driver.get(f"https://ww1.jujustukaisen.com/manga/jujustu-kaisen-chapter-{i}/")

# Find all image elements using the given CSS selector
image_elements = driver.find_elements(By.CSS_SELECTOR, ".entry-inner p img")

# Create a directory to save the images
if not os.path.exists('images'):
    os.makedirs('images')

for index, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute("src")
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_name = f"image_{index + 1}.jpg"
            image_path = os.path.join('images', image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {image_url} -> {image_name}")
        else:
            print(f"Failed to download: {image_url}")
    else:
        print("No src attribute found for an image element")

driver.quit()
