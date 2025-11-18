import time
from utils.driver import create_driver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_happy():
    driver = create_driver()
    page = LoginPage(driver)

    # ambil email hasil register sebelumnya
    with open("last_registered_email.txt", "r") as f:
        email = f.read().strip()

    page.open()

    page.login(
        email=email,
        password="testing123"
    )

    time.sleep(5)

    # Cek login berhasil dengan mendeteksi tombol Logout
    logout_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary")
    assert logout_btn.is_displayed()

    # (optional) cek teks "Signed in as"
    assert "Signed in as" in driver.page_source

    driver.quit()

