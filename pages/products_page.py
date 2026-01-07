class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('.title')
        self.cart_badge = page.locator('.shopping_cart_badge')

    async def is_loaded(self):
        await self.title.wait_for()
        return await self.title.inner_text() == "Products"

    async def add_product(self, product_test_id):
        await self.page.click(f'[data-test="{product_test_id}"]')

    async def cart_count(self):
        return await self.cart_badge.inner_text()
