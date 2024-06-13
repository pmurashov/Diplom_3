import allure

from locators.locators import MyAccountPageLocators
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form_visible(self):
        return self.check_element(MyAccountPageLocators.MY_ACCOUNT_FORM)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on_button(MyAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_on_logout_button(self):
        self.click_on_button(MyAccountPageLocators.LOGOUT_BUTTON)
