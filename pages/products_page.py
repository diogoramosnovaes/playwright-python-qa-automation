class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('.title')
        self.cart_badge = page.locator('.shopping_cart_badge')

    def is_loaded(self):
        self.title.wait_for()
        return self.title.inner_text() == "Products"

    def add_product(self, product_test_id):
        self.page.click(f'[data-test="{product_test_id}"]')

    def cart_count(self):
        return self.cart_badge.inner_text()
