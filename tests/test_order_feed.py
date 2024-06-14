import allure
import pytest

from helpers.helpers import Order
from locators.locators import OrderFeedLocators
from pages.main_page import HeaderPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('После клика на заказ, открывается всплывающее окно с деталями')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Клик на кнопку "Лента заказов"
                        3. Клик на 1 заказ
                        4. Проверка отображения формы с деталями заказа
                        ''')
    def test_order_info_window(self, driver):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_feed_button()
        feed_order.click_on_order_info()
        assert feed_order.check_order_info_window_visible()

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('''
                        1. Создаем пользователя через API
                        2. Переходим на страницу сервиса
                        3. Логин в систему
                        4. Переход на страницу "Лента заказов"
                        5. Получаем заказ в списке "В работе"
                        6. Получаем список заказов пользователя
                        7. Проверяем, что заказ пользователя в списке заказов "В работе"
                        8. Удаляем пользователя через API
                        ''')
    def test_user_order_in_progress(self, driver, create_new_user, login):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_feed_button()
        order.create_order(create_new_user)
        orders_in_progress = feed_order.get_in_progress_orders()
        user_order = str(order.get_user_orders(create_new_user))
        assert user_order in orders_in_progress

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('''
                        1. Создаем пользователя через API
                        2. Создаем заказ через API
                        2. Переходим на страницу сервиса
                        3. Логин в систему
                        4. Переход на страницу "Лента заказов"
                        5. Получаем заказа пользователя через API
                        6. Получаем список заказов на странице "Лента заказов"
                        7. Проверяем отображения заказа пользователя
                        8. Удаляем пользователя через API
                        ''')
    def test_user_orders_in_orders_history(self, driver, create_new_user, create_order, login):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_feed_button()
        user_order = str(order.get_user_orders(create_new_user))
        orders_history_in_feed = feed_order.get_orders_history()
        assert user_order in orders_history_in_feed

    @allure.title('При создании нового заказа счетчик Выполнено за всё время / Выполнено за сегодня увеличивается')
    @pytest.mark.parametrize('counter',
                             [OrderFeedLocators.TODAY_ORDERS_COUNTER, OrderFeedLocators.TOTAL_ORDERS_COUNTER])
    def test_update_counter_orders(self, driver, create_new_user, login, counter):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_feed_button()
        now_counter = int(feed_order.check_counter_orders(counter))
        order.create_order(create_new_user)
        new_counter = int(feed_order.check_counter_orders(counter))
        assert new_counter > now_counter
