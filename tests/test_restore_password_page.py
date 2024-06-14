import allure

from data.urls import Urls, Endpoints
from helpers.user_data import Person
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.restore_password_page import RestorePasswordPage


class TestRestorePasswordPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        ''')
    def test_redirect_to_restore_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_password_page = RestorePasswordPage(driver)
        main_page.move_to_personal_account_button_and_click()
        login_page.click_on_restore_password_button()
        assert restore_password_page.check_recovery_form() and restore_password_page.get_current_url() == (
                Urls.MAIN_URL + Endpoints.RESTORE_PASSWORD)

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        4. Заполнение поля "Email"
                        5. Клик на кнопку "Восстановить"
                        ''')
    def test_enter_password_and_click_on_recovery_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_password_page = RestorePasswordPage(driver)
        main_page.move_to_personal_account_button_and_click()
        login_page.click_on_restore_password_button()
        restore_password_page.send_keys_to_email_input(Person.create_data_correct_user()["email"])
        restore_password_page.click_on_restore_password_button()
        assert restore_password_page.check_save_button_visible() and restore_password_page.get_current_url() == (
                Urls.MAIN_URL + Endpoints.RESET_PASSWORD)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным"')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        4. Заполнение поля "Email"
                        5. Клик на кнопку "Восстановить"
                        6. Заполнить поле "Пароль"
                        7. Клик на кнопку "Показать"
                        ''')
    def test_password_input_highlight(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_password_page = RestorePasswordPage(driver)
        person_data = Person().create_data_correct_user()
        main_page.move_to_personal_account_button_and_click()
        login_page.click_on_restore_password_button()
        restore_password_page.send_keys_to_email_input(person_data.get("email"))
        restore_password_page.click_on_restore_password_button()
        assert restore_password_page.check_password_input_active(person_data.get("password"))
