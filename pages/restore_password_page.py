import allure

from pages.base_page import BasePage
from locators.locators import RestorePasswordPageLocators


class RestorePasswordPage(BasePage):
    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        return self.check_element(RestorePasswordPageLocators.RESTORE_PASSWORD_FORM)

    @allure.step('Заполнение формы Email')
    def send_keys_to_email_input(self, email):
        self.send_keys_to_input(RestorePasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_on_restore_password_button(self):
        self.click_on_button(RestorePasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Клик по кнопке Войти')
    def click_on_login_button(self):
        self.click_on_button(RestorePasswordPageLocators.LOG_IN_BUTTON)

    @allure.step('Заполнение поля Пароль')
    def send_keys_to_password_input(self, password):
        self.send_keys_to_input(RestorePasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Заполнение поля Код из письма')
    def send_keys_to_code_input(self, code):
        self.send_keys_to_input(RestorePasswordPageLocators.SECURITY_CODE, code)

    @allure.step('Клик по кнопке Сохранить')
    def click_on_save_button(self):
        self.click_on_button(RestorePasswordPageLocators.SAVE_BUTTON)

    @allure.step('Проверка подсветки поля Пароль')
    def check_password_input_active(self, password):
        self.send_keys_to_password_input(password)
        self.click_on_button(RestorePasswordPageLocators.SHOW_PASSWORD_BUTTON)
        return self.check_element(RestorePasswordPageLocators.PASSWORD_INPUT_HIGHLIGHTER)

    @allure.step('Проверка отображения кнопки Сохранить')
    def check_save_button_visible(self):
        return self.check_element(RestorePasswordPageLocators.SAVE_BUTTON)
