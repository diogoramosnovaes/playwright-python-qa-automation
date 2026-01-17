class CheckoutPage:
    def __init__(self, page):
        self.page = page

        # Selectors
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.success_message = page.locator('.complete-header')

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.wait_for()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish(self):
        self.finish_button.wait_for()
        self.finish_button.click()

    def success_text(self) -> str:
        self.success_message.wait_for()
        return self.success_message.inner_text()
