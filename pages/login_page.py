class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, user, password):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()
