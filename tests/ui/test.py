def test_saucedemo(page):
    page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in page.title()


def test_login_sucesso(page,base_url):
    page.goto(base_url)
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    titulo = page.locator('.title').inner_text()
    assert "Products" in titulo


def test_login_sucesso2(page, base_url):
    page.goto(base_url)

    login = page.locator('[data-test="username"]')
    senha = page.locator('[data-test="password"]')
    botao = page.locator('[data-test="login-button"]')

    login.fill("standard_user")
    senha.fill("secret_sauce")
    botao.click()

    titulo = page.locator('.title')
    titulo.wait_for()

    assert titulo.inner_text() == "Products"


def test_login_invalido(page):
    page.goto("https://www.saucedemo.com/")

    page.fill('[data-test="username"]', "invalid_user")
    page.fill('[data-test="password"]', "invalid_pass")
    page.click('[data-test="login-button"]')

    erro = page.locator('h3[data-test="error"]').inner_text()
    assert "Epic sadface" in erro

def test_adicionar_produtos_carrinho(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')

    # Adicionando produtos
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')

    # Validar contador
    contador = page.locator('.shopping_cart_badge').inner_text()
    assert contador == "2"

def test_checkout_completo(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[class="shopping_cart_link"]')

    page.click('[data-test="checkout"]')
    page.fill('[data-test="firstName"]', "Diogo")
    page.fill('[data-test="lastName"]', "QA")
    page.fill('[data-test="postalCode"]', "12345")

    page.click('[data-test="continue"]')
    page.click('[data-test="finish"]')

    mensagem = page.locator('.complete-header').inner_text()
    assert "Thank you for your order!" in mensagem