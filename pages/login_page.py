class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error = page.locator('h3[data-test="error"]')

    async def open(self, base_url):
        await self.page.goto(base_url)

    async def login(self, user, password):
        await self.username.fill(user)
        await self.password.fill(password)
        await self.login_button.click()

    async def get_error_message(self):
        return await self.error.inner_text()
