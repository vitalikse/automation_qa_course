from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
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
        assert radio_button_page.click_radio_button('yes') == radio_button_page.get_output(), "'Yes' have not been selected"
        assert radio_button_page.click_radio_button('impressive') == radio_button_page.get_output(), "'Impressive' have not been selected"
        assert radio_button_page.click_radio_button('no') == radio_button_page.get_output(), "'No' have not been selected"
        time.sleep(5)
