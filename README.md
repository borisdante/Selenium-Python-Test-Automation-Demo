# Automated Testing Demos

This repository contains examples of automated testing scripts created using Python. Each script demonstrates automation techniques for different use cases, including web testing and video game testing.

## Included Tests

### **1. Selenium Login Test**
- **File:** `selenium_login_test.py`
- **Description:**
  Automates testing a web login page. It verifies the presence of login elements (username, password fields, and login button), simulates entering user credentials, and submits the form to ensure proper navigation.

  **Features:**
  - Checks for required input fields.
  - Simulates user input.
  - Verifies login button functionality.

### **2. Selenium Complex Test**
- **File:** `selenium_complex_test.py`
- **Description:**
  Automates a more complex workflow in a web application. This includes navigation through multiple pages, interacting with various elements (dropdowns, forms, etc.), and validating outputs like success messages.

  **Features:**
  - Simulates end-to-end workflows.
  - Interacts with dynamic elements.
  - Captures screenshots for validation.

### **3. Shooter Game Automation Test**
- **File:** `shooter_automation_test.py`
- **Description:**
  Automates gameplay interactions in a shooter video game. It simulates movement, aiming, shooting, sprinting, and interacting with in-game objects. The script also captures screenshots for manual verification of game states.

  **Features:**
  - Simulates WASD movements for navigation.
  - Randomized mouse movements for aiming.
  - Simulates shooting (left mouse clicks) and interacting with objects (pressing 'E').
  - Captures and saves a screenshot for validation.

  **Requirements:**
  - The game must run in **windowed mode** for interaction.
  - Install `PyAutoGUI` for automation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/automated-testing-demos.git
   cd automated-testing-demos

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Ensure you have the required tools for each test:
    ```bash
    For Selenium: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
    For PyAutoGUI: Ensure your game runs in windowed mode.
    
