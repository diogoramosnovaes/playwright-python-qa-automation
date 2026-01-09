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

@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest.fixture
async def page(browser):
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()
