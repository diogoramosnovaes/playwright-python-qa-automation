class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')

    def open(self):
        self.page.click('.shopping_cart_link')

    def checkout(self):
        self.checkout_button.click()
