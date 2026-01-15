import pytest
from playwright.async_api import async_playwright

@pytest.fixture
async def api_request_context():
    async with async_playwright() as p:
        context = await p.request.new_context(
            base_url="https://petstore.swagger.io/v2"
        )
        yield context
        await context.dispose()

import pytest
import os
from datetime import datetime
from playwright.async_api import async_playwright

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            nome = item.nodeid.replace("::", "_").replace("/", "_")
            data = datetime.now().strftime("%Y%m%d_%H%M%S")
            caminho = f"screenshots/{nome}_{data}.png"

            import asyncio
            asyncio.get_event_loop().run_until_complete(
                page.screenshot(path=caminho, full_page=True)
            )

import pytest
from playwright.async_api import async_playwright

@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        await browser.close()

@pytest.fixture
async def page(browser, base_url):
    context = await browser.new_context(base_url=base_url)
    page = await context.new_page()
    yield page
    await context.close()

@pytest.fixture(scope="session")
def base_url():
    from config import get_base_url
    return get_base_url()