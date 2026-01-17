class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def open(self):
        self.cart_link.wait_for()
        self.cart_link.click()

    def checkout(self):
        self.checkout_button.wait_for()
        self.checkout_button.click()
