from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

class HistoryPage:

    menu_option = (By.CLASS_NAME, "fa-bars")

    field_history = (By.XPATH, "//a[@href='history.php#history']")

    confirm_history_facility = (By.ID, "facility")

    field_logout = (By.XPATH, "//a[@href='authenticate.php?logout']")

    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        self.driver.find_element(*self.menu_option).click()

    def click_history(self):
        history = self.driver.find_element(*self.field_history)
        self.driver.execute_script("arguments[0].click();", history)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.field_history)).click()
        # self.driver.find_element(*self.field_history).click()

    def history_facility_confirmation(self):
        return self.driver.find_element(*self.confirm_history_facility).text

    def click_logout(self):
        logout = self.driver.find_element(*self.field_logout)

        self.driver.execute_script(
            "arguments[0].click();", logout
        )

        
