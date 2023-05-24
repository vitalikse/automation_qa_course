from pages.elements_page import TextBoxPage
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_addr, output_per_addr = text_box_page.check_fillid_form()
            assert full_name == output_name, "The full name doesn't match"
            assert email == output_email, "The email doesn't match"
            assert current_address == output_current_addr, "The current address doesn't match"
            assert permanent_address == output_per_addr, "The permanent address doesn't match"
