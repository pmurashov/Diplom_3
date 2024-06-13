import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание загрузки элемента")
    def wait_for_element_loaded(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    @allure.step("Клик по кнопке")
    def click_on_button(self, locator):
        self.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Заполнение формы")
    def send_keys_to_input(self, locator, text):
        self.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text_locator(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step("Получение текста элементов")
    def get_text_locators(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Проверка отображения элемента")
    def check_element(self, locator):
        self.wait_for_element_loaded(locator)
        return self.driver.find_element(*locator)

    @allure.step("Проверка отсутствия элемента")
    def check_element_is_not_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Drag and drop элемента")
    def drag_and_drop(self, drag, drop):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(drag))
        target = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(drop))
        self.driver.execute_script("""
                           var source = arguments[0];
                           var target = arguments[1];
                           var evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                       """, element, target)

    @allure.step("Переход к элементу и клик на него")
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
