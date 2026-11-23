from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AppointmentPage:

    facility_dropdown = (By.ID, "combo_facility")

    program_radio = (By.ID, "radio_program_medicare")

    date_textbox = (By.ID, "txt_visit_date")

    comment_textbox = (By.ID, "txt_comment")

    book_appointment_button = (By.ID, "btn-book-appointment")

    appointment_confirmation_message = (By.XPATH, "//h2[text()='Appointment Confirmation']")

    confirm_facility = (By.ID, "facility")

    confirm_program = (By.ID, "program")

    confirm_date = (By.ID, "visit_date")

    confirm_comment = (By.ID, "comment")


    def __init__(self, driver):
        self.driver = driver

    def select_facility(self, facility_name):
        facility = Select(self.driver.find_element(*self.facility_dropdown))
        facility.select_by_visible_text(facility_name)

    def select_program_radio(self):
        self.driver.find_element(*self.program_radio).click()

    def enter_date(self, date_text):
        self.driver.find_element(*self.date_textbox).send_keys(date_text)

    def enter_comment(self, comment_text):
        self.driver.find_element(*self.comment_textbox).send_keys(comment_text)

    def click_book_appointment_button(self):
        self.driver.find_element(*self.book_appointment_button).click()

    def get_appointment_confirmation_message(self):
        return self.driver.find_element(*self.appointment_confirmation_message).text

    def facility_confirmation(self):
        return self.driver.find_element(*self.confirm_facility).text

    def program_confirmation(self):
        return self.driver.find_element(*self.confirm_program).text

    def date_confirmation(self):
        return self.driver.find_element(*self.confirm_date).text

    def comment_confirmation(self):
        return self.driver.find_element(*self.confirm_comment).text




