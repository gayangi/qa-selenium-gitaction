import os
from pages.login_page import LoginPage
from utils.driver_setup import get_driver

BASE_URL = "https://practicetestautomation.com/practice-test-login/"
SCREENSHOT_DIR = "screenshots"


def take_screenshot(driver, name):
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    driver.save_screenshot(f"{SCREENSHOT_DIR}/{name}.png")


def test_invalid_credentials_shows_error():
    driver = get_driver()
    login = LoginPage(driver)

    try:
    login.load(BASE_URL)
    login.enter_username("wrongUser")
    login.enter_password("wrongPass")
    login.click_login()

    error = login.get_error_text()
    assert error is not None and "success" in error.lower()

except Exception:
    take_screenshot(driver, "invalid_login_error")
    raise

finally:
    driver.quit()
