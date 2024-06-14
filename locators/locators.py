from selenium.webdriver.common.by import By


class HeaderPageLocatrors:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")  # Кнопка конструктор
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")  # Кнопка лента заказов
    MY_ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")  # Кнопка личный кабинет


class MainPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")  # Форма ленты заказа
    CONSTRUCTOR_FORM = (
        By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")  # Форма конструктора
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформить заказ
    FLUORESCENT_BUN_BUTTON = (
    By.XPATH, ".//img[@src='https://code.s3.yandex.net/react/code/bun-01.png']")  # Кнопка флюорисцентной булки
    POPUP_FORM_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')  # Крестик на модульном окне
    INGREDIENT_BUTTON = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")  # Счетчик ингредиента
    ORDER_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")  # Форма оформленного заказа
    SHOPPING_CART = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")  # Корзина
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")  # Номер заказа
    MY_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка личного кабинета
    INGREDIENTS_POPUP_FORM = (By.XPATH, "//h2[text()= 'Детали ингредиента']")  # Форма флюорисцентной булки


class AuthorizationPageLocators:
    LOGIN_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    LOG_IN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка войти
    REGISTER_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка зерегистрироваться
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка восстановить пароль


class RestorePasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    RESTORE_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка восстановить
    LOG_IN_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")  # Поле ввода нового пароля
    SECURITY_CODE = (By.XPATH, ".//label[text() = 'Введите код из письма']")  # Поле ввода кода из письма
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка Сохранить
    RESTORE_PASSWORD_FORM = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")  # ФОрма восстановления пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")  # Показать пароль
    PASSWORD_INPUT_HIGHLIGHTER = (By.CSS_SELECTOR, ".input.input_status_active")  # Подсветка поля пароль


class MyAccountPageLocators:
    MY_ACCOUNT_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма личного кабинета
    PROFILE_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка профиль
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка история заказов
    ORDER_HISTORY_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")  # Форма истории заказов
    ORDER_ID = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")  # Номер заказа
    CANCEL_BUTTON = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка отмена
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранить
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выход


class OrderFeedLocators:
    title_orders_list = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок страницы
    ORDER_DETAILS_WINDOW = (By.XPATH, '//p[text()="Cостав"]')  # Окно детали заказа
    TOTAL_ORDERS_COUNTER = (
        By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик заказов за все время
    TODAY_ORDERS_COUNTER = (
        By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Счетчик заказов за сегодня
    IN_PROGRESS_ORDERS = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")  # Заказы "В работе"
    ORDER_INFO_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")  # 1 заказ в истории
    ORDER_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')  # Все заказы в истории
