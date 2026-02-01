import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=500
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser, base_url):
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def api():
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url="https://petstore.swagger"
        )
        yield context
        context.dispose()
