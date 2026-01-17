class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def is_loaded(self) -> bool:
        self.title.wait_for()
        return self.title.inner_text() == "Products"

    def add_product(self, product_test_id: str):
        button = self.page.locator(f'[data-test="{product_test_id}"]')
        button.wait_for()
        button.click()

    def cart_count(self) -> str:
        self.cart_badge.wait_for()
        return self.cart_badge.inner_text()

