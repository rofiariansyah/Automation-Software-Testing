import random
import time
from utils.driver import create_driver
from pages.register_page import RegisterPage

def test_register_happy():
    driver = create_driver()
    page = RegisterPage(driver)

    page.open()

    random_num = random.randint(1000, 9999)
    email = f"rofi{random_num}@mail.com"

    page.register(
        name="Rofi",
        email=email,
        phone="08123456789",
        password="testing123"
    )

    time.sleep(3)

    # simpan email ke file
    with open("last_registered_email.txt", "w") as f:
        f.write(email)

    assert "login" in driver.current_url.lower()

    driver.quit()

