class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.success_message = page.locator('.complete-header')

    async def fill_form(self, first, last, zip):
        await self.first_name.fill(first)
        await self.last_name.fill(last)
        await self.postal_code.fill(zip)
        await self.continue_button.click()

    async def finish(self):
        await self.finish_button.click()

    async def success_text(self):
        return await self.success_message.inner_text()
