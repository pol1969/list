from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_items(self):
        ''' тест : нельзя добавлять пустые элементы списка '''
        # Эдит открывает домашнюю страницу т случайно пытается отправить
        # пустой элемент списка. Оша нажимает Enter на пустом поле ввода
#       self.assertEqual(
#           self.browser.find_element_by_css_selector('.has-error').text,
#           "You can't have empty list item"
#               )

        # Домашняя страница обновляется и появляется сообщенин об ошибке,
        # которое говорит, что элементы списка не должны быть пустыми
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have empty list item"
                ))


        # Она пробует снова, теперь с неким текстом для элемента, и теперь
        # это срабатывает
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_list_in_table('1: Buy milk')

        # Как ни странно, Эдит решает отправить второй пустой элемент списка
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        # Она получает аналогичное предупреждение на странице списка
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have empty list item"
                ))


        # И она может его исправить, заполнив поле неким текстом
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_list_in_table('1: Buy milk')
        self.wait_for_list_in_table('2: Make tea')



