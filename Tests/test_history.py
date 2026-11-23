from Pages.LoginPage import LoginPage
from Pages.AppointmentPage import AppointmentPage
from Pages.HistoryPage import HistoryPage
from time import sleep

def test_history(setup):

    login_page = LoginPage(setup)
    appointment_page = AppointmentPage(setup)
    history_page = HistoryPage(setup)

    login_page.open_page()
    login_page.click_make_appointment_button()
    login_page.login(
        username="John Doe",
        password="ThisIsNotAPassword"
    )

    appointment_page.select_facility("Tokyo CURA Healthcare Center")
    appointment_page.select_program_radio()
    appointment_page.enter_date("11/11/2000")
    appointment_page.enter_comment("Test Comment")
    appointment_page.click_book_appointment_button()
    sleep(2)

    history_page.click_menu()
    history_page.click_history()

    assert history_page.history_facility_confirmation() == "Tokyo CURA Healthcare Center"


