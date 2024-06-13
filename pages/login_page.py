import allure
from pages.base_page import BasePage
from locators.locators import AuthorizationPageLocators


class LoginPage(BasePage):
    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        return self.check_element(AuthorizationPageLocators.LOGIN_FORM)

    @allure.step('Заполнение поля "Email"')
    def send_keys_to_email_input(self, email):
        self.send_keys_to_input(AuthorizationPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_input(self, password):
        self.send_keys_to_input(AuthorizationPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_on_login_button(self):
        self.move_to_element_and_click(AuthorizationPageLocators.LOG_IN_BUTTON)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.send_keys_to_email_input(email)
        self.send_password_to_password_input(password)
        self.click_on_login_button()

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_on_restore_password_button(self):
        self.move_to_element_and_click(AuthorizationPageLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Клик на кнопку "Зарегистрироваться"')
    def click_on_register_button(self):
        self.move_to_element_and_click(AuthorizationPageLocators.REGISTER_BUTTON)
