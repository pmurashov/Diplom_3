import allure

from locators.locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Получение количества заказов')
    def check_counter_orders(self, locators):
        return self.get_text_locator(locators)

    @allure.step('Клик на 1 заказ в "Лента заказов"')
    def click_on_order_info(self):
        self.click_on_button(OrderFeedLocators.ORDER_INFO_WINDOW)

    @allure.step('Проверка видимости формы заказа')
    def check_order_info_window_visible(self):
        return self.check_element(OrderFeedLocators.ORDER_DETAILS_WINDOW)

    @allure.step('Получение заказов "В работе"')
    def get_in_progress_orders(self):
        elements = self.get_text_locators(OrderFeedLocators.IN_PROGRESS_ORDERS)
        orders_list = []
        for element in elements:
            order_number = element.text[1:]
            orders_list.append(order_number)
        return orders_list

    @allure.step('Получение номеров заказов')
    def get_orders_history(self):
        elements = self.get_text_locators(OrderFeedLocators.ORDER_HISTORY)
        orders_list = []
        for element in elements:
            order_number = element.text[2:]
            orders_list.append(order_number)
        return orders_list
