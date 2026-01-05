class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.success_message = page.locator('.complete-header')

    def fill_form(self, first, last, zip):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip)
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()

    def success_text(self):
        return self.success_message.inner_text()
