from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set path to your ChromeDriver executable
webdriver_service = Service('C:/Users/yaswa/Downloads/chromedriver_win32 (1)')

# Launch Chrome browser
driver = webdriver.Chrome(service=webdriver_service)

try:
    # Open the webpage
    driver.get("https://yaswanthreddys.in/DistanceGuru%20Project/card.html")

    # Find the input fields
    from_input = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, "from_places")))
    to_input = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, "to_places")))
    to_button = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, "but1")))

    # Enter values in the input fields
    from_input.send_keys("Vijayawada")

    # Wait for the "to" input field to become clickable
    to_input = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, "to_places")))
    to_input.send_keys("Bapatla")

    # Find and click the submit button
    submit_button = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, "but1")))
    submit_button.click()

    # Wait for the result to be displayed
    distance_result = WebDriverWait(driver, 90).until(EC.visibility_of_element_located((By.ID, "distanceResult")))

    # Retrieve and print the distance result
    print("Distance Result:", distance_result.text)

finally:
    # Close the browser
    driver.quit()