import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.asyncio
async def test_saucedemo(page):
    await page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in await page.title()


@pytest.mark.asyncio
async def test_login_sucesso(page, base_url):
    login = LoginPage(page)
    products = ProductsPage(page)

    await login.open(base_url)
    await login.login("standard_user", "secret_sauce")

    assert await products.is_loaded()


@pytest.mark.asyncio
async def test_login_invalido(page, base_url):
    login = LoginPage(page)

    await login.open(base_url)
    await login.login("invalid_user", "invalid_pass")

    assert "Epic sadface" in await login.get_error_message()


@pytest.mark.asyncio
async def test_adicionar_produtos_carrinho(page, base_url):
    login = LoginPage(page)
    products = ProductsPage(page)

    await login.open(base_url)
    await login.login("standard_user", "secret_sauce")

    await products.add_product("add-to-cart-sauce-labs-backpack")
    await products.add_product("add-to-cart-sauce-labs-bike-light")

    assert await products.cart_count() == "2"


@pytest.mark.asyncio
async def test_checkout_completo(page, base_url):
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    await login.open(base_url)
    await login.login("standard_user", "secret_sauce")

    await products.add_product("add-to-cart-sauce-labs-backpack")
    await products.add_product("add-to-cart-sauce-labs-bike-light")

    assert await products.cart_count() == "2"

    await cart.open()
    await cart.checkout()

    await checkout.fill_form("Diogo", "QA", "12345")
    await checkout.finish()

    assert "Thank you for your order!" in await checkout.success_text()