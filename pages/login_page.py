from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://test-automation.kartala.dev/login"

        self.input_email = (By.NAME, "email")
        self.input_password = (By.NAME, "password")
        self.btn_login = (By.CSS_SELECTOR, ".btn.btn-primary")
        self.error_msg = (By.CSS_SELECTOR, ".alert.alert-danger")

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.driver.find_element(*self.input_email).send_keys(email)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
