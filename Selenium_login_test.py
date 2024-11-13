from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_login_test():
    # Set up the WebDriver (ensure you have the appropriate driver installed and in PATH)
    driver = webdriver.Chrome()  # Or use the appropriate WebDriver for your browser

    # Open the login page
    driver.get("https://example.com/login")  # Replace with your actual login page URL

    # Find the username and password fields and enter credentials
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("testuser")  # Use a valid test username
    password_field.send_keys("password")  # Use a valid test password

    # Submit the form (e.g., using the Enter key)
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to allow for the page to load
    time.sleep(3)

    # Check if login was successful by verifying the new page URL or a logged-in element
    # Here we check for a successful login by looking for a specific element that is visible only after login
    try:
        logged_in_element = driver.find_element(By.ID, "welcome-message")  # Update with actual element after login
        print("Test Passed: Login successful!")
    except:
        print("Test Failed: Login unsuccessful.")

    # Close the browser
    driver.quit()

# Run the login test
if __name__ == "__main__":
    run_login_test()
