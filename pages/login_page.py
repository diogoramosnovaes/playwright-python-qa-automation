class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error = page.locator('h3[data-test="error"]')

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, user, password):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error.inner_text()
