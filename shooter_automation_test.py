import pyautogui
import time
import random

def test_shooter_game():
    """
    Automates basic gameplay interactions in a shooter video game:
    - Movement (WASD keys).
    - Aiming and shooting (mouse movements and clicks).
    - Interaction with objects (pressing 'E').
    - Screen region validation (e.g., checking for enemy icons or health bars).
    """
    print("Starting shooter game automation test...")
    
    # Wait for the game to load
    print("Make sure the game is running in windowed mode.")
    time.sleep(5)  # Adjust based on game loading time

    # Simulate movement (WASD keys for navigation)
    print("Simulating movement...")
    for _ in range(5):
        pyautogui.press("w")  # Move forward
        time.sleep(1)
        pyautogui.press("a")  # Strafe left
        time.sleep(1)
        pyautogui.press("d")  # Strafe right
        time.sleep(1)
        pyautogui.press("s")  # Move backward
        time.sleep(1)

    # Simulate aiming (mouse movements)
    print("Simulating aiming...")
    for _ in range(10):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        pyautogui.moveRel(x, y, duration=0.1)  # Randomized mouse movements to simulate aiming
        time.sleep(0.1)

    # Simulate shooting (left mouse button clicks)
    print("Simulating shooting...")
    for _ in range(5):
        pyautogui.click()  # Simulate firing a shot
        time.sleep(0.5)

    # Simulate interacting with an object (pressing 'E' to pick up items or open doors)
    print("Simulating interaction...")
    for _ in range(3):
        pyautogui.press("e")  # Simulate interaction key
        time.sleep(1)

    # Simulate sprinting (holding down 'Shift' + 'W')
    print("Simulating sprinting...")
    pyautogui.keyDown("shift")  # Hold down the sprint key
    pyautogui.press("w")
    time.sleep(2)  # Sprint for 2 seconds
    pyautogui.keyUp("shift")

    # Capture the screen to verify game state
    print("Capturing screen for validation...")
    screenshot = pyautogui.screenshot(region=(100, 100, 800, 600))  # Adjust region for your game
    screenshot.save("shooter_test_screenshot.png")
    print("Screenshot saved. Manually verify game state.")

    print("Shooter game automation test completed.")

if __name__ == "__main__":
    test_shooter_game()
