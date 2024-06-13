import allure

from data.urls import Urls, Endpoints
from pages.main_page import MainPage, HeaderPage


class TestMainPage:
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Клик по кнопке "Войти в аккаунт"
                        3. Клик по кнопке "Конструктор"
                        4. Проверка отображения формы "Конструктор"
                        ''')
    def test_redirect_to_constructor_page(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.move_to_personal_account_button_and_click()
        header.click_on_constructor_button()
        assert main_page.check_constructor_form_visible() and main_page.get_current_url() == Urls.MAIN_URL

    @allure.title('Переход по клику на «Лента заказов»')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Клик по кнопке "Лента заказов"
                        3. Проверка отображения формы "Лента заказов"
                        ''')
    def test_redirect_to_orders_feed_page(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_on_feed_button()
        assert main_page.check_orders_feed_form() and main_page.get_current_url() == (Urls.MAIN_URL + Endpoints.FEED)

    @allure.title('Появление всплывающего окна с деталями с деталями ингредиента')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Клик по кнопке "Флюорисцентная булка R2-D3
                        3. Проверка отображения высплывающего окна с деталями ингредиента
                        ''')
    def test_fluorescent_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_fluorescent_bun_button()
        assert main_page.check_fluorescent_bun_form_visible()

    @allure.title('Закрытие всплывающего окна')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Клик по кнопке "Флюорисцентная булка R2-D3
                        3. Клик по крестику модального окна
                        4. Проверка закрытия формы "Информация об ингредиенте"
                        ''')
    def test_close_fluorescent_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_fluorescent_bun_button()
        main_page.close_ingredient_info_popup_form()
        assert main_page.check_fluorescent_bun_form_closed()

    @allure.title('При добавлении ингредиента в заказ счётчик ингридиента увеличивается')
    @allure.description('''
                        1. Переход на страницу сервиса
                        2. Добавление "Флюорисцентная булка R2-D3 в корзину"
                        3. Проверка увеличения счетчика ингредиента
                        ''')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_bun_to_shopping_cart()
        assert int(main_page.check_ingredient_counter()) > 0

    @allure.title('Авторизованный пользователь может оформить заказ')
    @allure.description('''
                        1. Создание пользователя через API
                        2. Переход на страницу сервиса
                        3. Авторизация под новым юзером в системе
                        4. Добавление "Флюорисцентная булка R2-D3" в корзину
                        5. Клик по кнопке "Оформить заказ"
                        6. Проверка отображения формы заказа
                        7. Удаление пользователя через API
                        ''')
    def test_create_order(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_on_constructor_button()
        main_page.create_order()
        assert main_page.check_order_form()
