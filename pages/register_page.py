from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://test-automation.kartala.dev/register"

        self.input_name = (By.NAME, "name")
        self.input_email = (By.NAME, "email")
        self.input_phone = (By.NAME, "phone")
        self.input_password = (By.NAME, "password")
        self.btn_submit = (By.CSS_SELECTOR, ".btn.btn-primary")
        self.error_msg = (By.CSS_SELECTOR, ".alert.alert-danger")

    def open(self):
        self.driver.get(self.url)

    def register(self, name, email, phone, password):
        self.driver.find_element(*self.input_name).send_keys(name)
        self.driver.find_element(*self.input_email).send_keys(email)
        self.driver.find_element(*self.input_phone).send_keys(phone)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.btn_submit).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
