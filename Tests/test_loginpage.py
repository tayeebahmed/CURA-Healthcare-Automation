from time import sleep

from Pages.LoginPage import LoginPage


def test_login_page(setup):
    driver = setup

    login_page = LoginPage(driver)

    login_page.open_page()
    login_page.click_make_appointment_button()
    login_page.enter_username_text("John Doe")
    login_page.enter_password_text("ThisIsNotAPassword")
    login_page.click_login_button()
    sleep(3)

    assert "appointment" in driver.current_url
