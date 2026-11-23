from selenium.webdriver.common.by import By


class LoginPage:

    make_appointment_button = (By.ID, "btn-make-appointment")

    username_textbox = (By.ID, "txt-username")

    password_textbox = (By.ID, "txt-password")

    login_button = (By.ID, "btn-login")


    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(
            "https://katalon-demo-cura.herokuapp.com/"
        )

    def click_make_appointment_button(self):
        self.driver.find_element(*self.make_appointment_button).click()

    def enter_username_text(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password_text(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username_text(username)
        self.enter_password_text(password)
        self.click_login_button()