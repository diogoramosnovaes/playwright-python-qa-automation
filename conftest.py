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
def api_request_context():
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url="https://petstore.swagger.io/v2"
        )
        yield context
        context.dispose()

@pytest.fixture(scope="session")
def api():
    with sync_playwright() as p:
        ctx = p.request.new_context(base_url="https://petstore.swagger.io")
        yield ctx
        ctx.dispose()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#
#     if result.when == "call" and result.failed:
#         page = item.funcargs.get("async_page")
#
#         if page:
#             os.makedirs("screenshots", exist_ok=True)
#
#             nome = item.nodeid.replace("::", "_").replace("/", "_")
#             data = datetime.now().strftime("%Y%m%d_%H%M%S")
#             caminho = f"screenshots/{nome}_{data}.png"
#
#             import asyncio
#
#             try:
#                 loop = asyncio.get_running_loop()
#             except RuntimeError:
#                 loop = asyncio.new_event_loop()
#                 asyncio.set_event_loop(loop)
#
#             loop.run_until_complete(
#                 page.screenshot(path=caminho, full_page=True)
#             )
