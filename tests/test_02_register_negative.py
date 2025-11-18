import time
from utils.driver import create_driver
from pages.register_page import RegisterPage

def test_register_negative():
    driver = create_driver()
    page = RegisterPage(driver)

    page.open()

    page.register(
        name="A",
        email="test@mail.com",
        phone="0812",
        password="password"
    )

    time.sleep(5)

    error = page.get_error_message()

    assert "minimal" in error.lower() or "2" in error.lower()

    driver.quit()
