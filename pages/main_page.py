import allure

from locators.locators import HeaderPageLocatrors
from locators.locators import MainPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.move_to_element_and_click(HeaderPageLocatrors.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_feed_button(self):
        self.move_to_element_and_click(HeaderPageLocatrors.ORDER_FEED_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_my_account_button(self):
        self.move_to_element_and_click(HeaderPageLocatrors.MY_ACCOUNT_BUTTON)


class MainPage(BasePage):
    @allure.step('Переход к кнопке "Личный Кабинет" и клик на нее')
    def move_to_personal_account_button_and_click(self):
        self.move_to_element_and_click(MainPageLocators.MY_ACCOUNT_BUTTON)

    @allure.step('Проверка отображения формы конструктор')
    def check_constructor_form_visible(self):
        return self.check_element(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        return self.check_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по Флюорисцентной булке RD-D3')
    def click_on_fluorescent_bun_button(self):
        self.click_on_button(MainPageLocators.FLUORESCENT_BUN_BUTTON)

    @allure.step('Проверка отображения формы "Информации о булке"')
    def check_fluorescent_bun_form_visible(self):
        return self.check_element(MainPageLocators.INGREDIENTS_POPUP_FORM)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_fluorescent_bun_form_closed(self):
        return self.check_element(MainPageLocators.INGREDIENTS_POPUP_FORM)

    @allure.step('Закрытие формы информации об ингридиенте')
    def close_ingredient_info_popup_form(self):
        self.move_to_element_and_click(MainPageLocators.POPUP_FORM_CLOSE_BUTTON)

    @allure.step('Добавить булку в корзину')
    def add_bun_to_shopping_cart(self):
        self.wait_for_element_clickable(MainPageLocators.FLUORESCENT_BUN_BUTTON)
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN_BUTTON, MainPageLocators.SHOPPING_CART)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_button(MainPageLocators.ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun_to_shopping_cart()
        self.click_on_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_ingredient_counter(self):
        return self.get_text_locator(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Проверка отображения формы Оформление заказа')
    def check_order_form(self):
        return self.check_element(MainPageLocators.ORDER_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_id(self):
        return self.get_text_locator(MainPageLocators.ORDER_ID)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_for_order_button_loaded(self):
        self.wait_for_element_loaded(MainPageLocators.ORDER_BUTTON)
