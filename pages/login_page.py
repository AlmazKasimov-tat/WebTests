from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_FIELD_PASSWORD = (By.ID, 'field_password')
    LOGIN_SUBMIT = "//button[@type='submit']"
    LOGIN_QR = "//button[contains(text(), 'Войти по QR-коду')]"
    LOGIN_CANT = "//button[contains(text(), 'Не получается войти?')]"
    SIGN_UP = "//button[contains(text(), 'Зарегистрироваться')]"
    SIGN_UP_VK = "//button[contains(text(), 'Войти через VK ID')]"
    SIGN_UP_MAIL = "//button[contains(text(), 'Войти через Почту')]"
    SIGN_UP_YANDEX = "//button[contains(text(), 'Войти через Яндекс')]"
    QR_CODE = "//button[contains(text(), 'QR-код')]"



class LoginPageHelper(BasePage):
    pass
