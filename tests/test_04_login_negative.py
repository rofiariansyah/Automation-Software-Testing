import time
from utils.driver import create_driver
from pages.login_page import LoginPage

def test_login_negative():
    driver = create_driver()
    page = LoginPage(driver)

    page.open()

    page.login(
        email="wrong@mail.com",
        password="salah123"
    )

    time.sleep(5)

    error = page.get_error_message()

    assert "invalid" in error.lower() or "error" in error.lower()

    driver.quit()
