class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'

class Endpoints:
    FEED = 'feed'  # Лента заказов
    LOGIN = 'login'  # Авторизация
    RESTORE_PASSWORD = 'forgot-password'  # Восстановление пароля
    MY_ACCOUNT = 'account/profile'  # Личный кабинет
    ORDER_HISTORY = 'account/order-history'  # История заказов
    RESET_PASSWORD = 'reset-password'  # Сброс пароля
    CREATE_USER = 'api/auth/register'  # Регистрация пользователя
    DELETE_USER = 'api/auth/user'  # Удаление пользователя
    CREATE_ORDER = 'api/orders'  # Создание заказа
    GET_ORDERS = 'api/orders'  # Получение заказов
