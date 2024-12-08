import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from Data.urls import Urls
from Data.data import ValidData


class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """При успешной регистрации перебрасывает на страницу входа"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistration.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistration.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistration.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistration.ar_register_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_element_with_login_text))

        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'
        

    def test_registration_empty_name_nothing_happens(self, driver):
        """ При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет """
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistration.ar_email_field).send_keys('test1@yan.ru')
        driver.find_element(*AuthRegistration.ar_password_field).send_keys('124567')

        driver.find_element(*AuthRegistration.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AuthRegistration.ar_register_button))
        WebDriverWait(driver, 2)
        errors_messages = driver.find_elements(*AuthRegistration.ar_error_message)

        assert driver.current_url == Urls.url_register and len(errors_messages) == 0
        


    @pytest.mark.parametrize('email_list', ['test1@yanru', 'test2yan.ru', 'te st3@yan.ru', 'test4@ya n.ru',
                                            '@yan.ru', 'test6@.ru', 'test7@yan.'])
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        """ При некорректном email появляется ошибка, что пользователь уже существует """
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistration.ar_name_field).send_keys('Goncharenko')
        driver.find_element(*AuthRegistration.ar_email_field).send_keys(email_list)
        driver.find_element(*AuthRegistration.ar_password_field).send_keys('123456')

        driver.find_element(*AuthRegistration.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistration.ar_error_message_2))
        error_message = driver.find_element(*AuthRegistration.ar_error_message_2)

        assert error_message.text == 'Такой пользователь уже существует'
        

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistration.ar_name_field).send_keys('Goncharenko')
        driver.find_element(*AuthRegistration.ar_email_field).send_keys('test1@yan.ru')
        driver.find_element(*AuthRegistration.ar_password_field).send_keys(password_list)

        driver.find_element(*AuthRegistration.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistration.ar_error_message))
        error_message = driver.find_element(*AuthRegistration.ar_error_message)

        assert error_message.text == 'Некорректный пароль'
        
