import random
import pytest
from tests.api.clients.petstore_client import PetStoreClient
from tests.api.models.pet_model import Pet

@pytest.mark.asyncio
async def test_criar_buscar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet = Pet(
        id=random.randint(1000, 9999),
        name="Dog QA",
        status="available"
    )

    response_create = await client.create_pet(pet)
    assert response_create.status == 200

    response_get = await client.get_pet(pet.id)
    assert response_get.status == 200

    pet_response = Pet.from_response(response_get.json())

    assert pet_response.name == pet.name
    assert pet_response.status == pet.status


@pytest.mark.asyncio
async def test_atualizar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet = Pet(
        id=random.randint(1000, 9999),
        name="Initial",
        status="available"
    )

    # Criação
    response_create = await client.create_pet(pet)
    assert response_create.status == 200

    # Atualização
    pet.name = "Updated"
    pet.status = "sold"

    response_update = await client.update_pet(pet)
    assert response_update.status == 200

    # ⚠️ json() é async no Playwright
    data = await response_update.json()

    pet_response = Pet.from_response(data)

    assert pet_response.status == "sold"
    assert pet_response.name == "Updated"

@pytest.mark.asyncio
async def test_deletar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet = Pet(
        id=random.randint(1000, 9999),
        name="Temp",
        status="available"
    )

    await client.create_pet(pet)

    response_delete = await client.delete_pet(pet.id)
    assert response_delete.status == 200

    response_get = await client.get_pet(pet.id)
    assert response_get.status == 404
