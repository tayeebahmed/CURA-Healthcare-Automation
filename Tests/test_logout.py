from Pages.LoginPage import LoginPage
from Pages.AppointmentPage import AppointmentPage
from Pages.HistoryPage import HistoryPage
from time import sleep

def test_logout(setup):

    login_page = LoginPage(setup)
    appointment_page = AppointmentPage(setup)
    history_page = HistoryPage(setup)

    login_page.open_page()
    login_page.click_make_appointment_button()
    login_page.login(
        username="John Doe",
        password="ThisIsNotAPassword"
    )

    # used to open the menu
    history_page.click_menu()
    history_page.click_logout()
    sleep(2)

    assert setup.current_url == "https://katalon-demo-cura.herokuapp.com/"
