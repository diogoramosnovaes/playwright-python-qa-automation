from playwright.sync_api import sync_playwright
import pytest
import os
from datetime import datetime
from config import get_base_url
from config import get_api_url

# 🧪 Hook para capturar screenshot ao final de cada teste
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            nome = item.nodeid.replace("::", "_").replace("/", "_")
            data = datetime.now().strftime("%Y%m%d_%H%M%S")
            caminho = f"screenshots/{nome}_{data}.png"

            page.screenshot(path=caminho, full_page=True)


# 🌍 Base URL configurável por ambiente
@pytest.fixture(scope="session")
def base_url():
    return get_base_url()


# 🌐 Navegador único para toda a execução
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()


# 🧪 Página isolada para cada teste
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    yield page

    # O fechamento ocorre somente após o hook executar
    context.close()


@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        ctx = p.request.new_context(base_url="https://petstore.swagger.io")
        yield ctx
        ctx.dispose()