import pytest
from playwright.sync_api import sync_playwright

client = "https://petstore.swagger.io/v2"
@pytest.fixture(scope="session")
def api():
    with sync_playwright() as p:
        ctx = p.request.new_context(base_url=client)
        yield ctx
        ctx.dispose()
def test_buscar_pets_disponiveis(api):
    response = api.get(client+"/pet/findByStatus?status=available")

    assert response.status == 200
    assert isinstance(response.json(), list)