class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')

    async def open(self):
        await self.page.click('.shopping_cart_link')

    async def checkout(self):
        await self.checkout_button.click()
