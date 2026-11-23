from time import sleep

from Pages.AppointmentPage import AppointmentPage
from Pages.LoginPage import LoginPage
from Pages.HistoryPage import HistoryPage

def test_appointment_page(setup):
    driver = setup

    history_page = HistoryPage(driver)

    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.click_make_appointment_button()
    login_page.login(
        username="John Doe",
        password="ThisIsNotAPassword"
    )

    appointment_page = AppointmentPage(driver)

    appointment_page.select_facility("Tokyo CURA Healthcare Center")
    appointment_page.select_program_radio()
    appointment_page.enter_date("11/11/2000")
    appointment_page.enter_comment("Test Comment")
    appointment_page.click_book_appointment_button()
    sleep(3)

    assert appointment_page.get_appointment_confirmation_message() == "Appointment Confirmation"
    assert appointment_page.facility_confirmation() == "Tokyo CURA Healthcare Center"
    assert appointment_page.program_confirmation() == "Medicare"
    assert appointment_page.date_confirmation() == "11/11/2000"
    assert appointment_page.comment_confirmation() == "Test Comment"

    # history_page.click_menu()
    # history_page.click_history()
    #
    # assert history_page.history_facility_confirmation() == "Tokyo CURA Healthcare Center"




