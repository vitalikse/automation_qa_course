import random

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "The full name doesn't match"
            assert email == output_email, "The email doesn't match"
            assert current_address.replace('\n', ' ') == output_current_addr, "The current address doesn't match"
            assert permanent_address.replace('\n', ' ') == output_per_addr, "The permanent address doesn't match"


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_check_box()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, 'checkboxes have not been selected'


class TestRadioButton:

    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        assert radio_button_page.click_radio_button(
            'yes') == radio_button_page.get_output(), "'Yes' have not been selected"
        assert radio_button_page.click_radio_button(
            'impressive') == radio_button_page.get_output(), "'Impressive' have not been selected"
        assert radio_button_page.click_radio_button(
            'no') == radio_button_page.get_output(), "'No' have not been selected"


class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, "The person was not found in the table"

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        print(age)
        print(row)
        assert age in row, "The person card has not been changed"

    def test_web_table_delete_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found"

    def test_web_table_change_count_row(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50,
                         100], "The number of rows in the table has not been changed or has changed incorrectly"
