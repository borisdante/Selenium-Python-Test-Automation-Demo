from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert

def run_complex_test():
    # Set up the WebDriver (ensure you have the appropriate driver installed and in PATH)
    driver = webdriver.Chrome()  # Or use the appropriate WebDriver for your browser

    # Navigate to the test form page
    driver.get("https://example.com/contact")  # Replace with your actual test form URL

    # Find the form fields and fill them out
    name_field = driver.find_element(By.NAME, "name")
    email_field = driver.find_element(By.NAME, "email")
    message_field = driver.find_element(By.NAME, "message")

    name_field.send_keys("John Doe")  # Sample name
    email_field.send_keys("john.doe@example.com")  # Sample email
    message_field.send_keys("This is a test message.")  # Sample message

    # Submit the form by pressing the Enter key or clicking the submit button
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Wait for the alert to appear after form submission
    time.sleep(2)

    # Handle the alert pop-up that appears after form submission
    try:
        alert = Alert(driver)
        alert_text = alert.text
        print(f"Alert text: {alert_text}")
        alert.accept()  # Accept the alert to close it
    except:
        print("No alert appeared after form submission.")

    # Wait for the page to load after form submission (wait for new page or response)
    time.sleep(3)

    # Check if we are redirected to a new page (check the page title or URL)
    new_page_title = driver.title
    if "Thank You" in new_page_title:  # Assuming the new page contains "Thank You" in the title
        print("Test Passed: Successfully submitted the form and reached the thank you page.")
    else:
        print("Test Failed: Did not reach the expected 'Thank You' page.")

    # Verify specific content on the new page (e.g., a confirmation message)
    try:
        confirmation_message = driver.find_element(By.XPATH, "//h1[text()='Thank you for your message!']")
        print("Confirmation message found: Test Passed!")
    except:
        print("Confirmation message not found: Test Failed!")

    # Close the browser
    driver.quit()

# Run the complex test
if __name__ == "__main__":
    run_complex_test()
