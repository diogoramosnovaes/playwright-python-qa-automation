from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_login_sucesso(page, base_url):
    login = LoginPage(page)
    products = ProductsPage(page)

    login.open(base_url)
    login.login("standard_user", "secret_sauce")

    assert products.is_loaded()

def test_login_invalido(page, base_url):
    login = LoginPage(page)

    login.open(base_url)
    login.login("invalid_user", "invalid_pass")

    assert "Epic sadface" in login.get_error_message()

def test_checkout_completo(page, base_url):
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.open(base_url)
    login.login("standard_user", "secret_sauce")

    products.add_product("add-to-cart-sauce-labs-backpack")
    products.add_product("add-to-cart-sauce-labs-bike-light")

    assert products.cart_count() == "2"

    cart.open()
    cart.checkout()

    checkout.fill_form("Diogo", "QA", "12345")
    checkout.finish()

    assert "Thank you for your order!" in checkout.success_text()
