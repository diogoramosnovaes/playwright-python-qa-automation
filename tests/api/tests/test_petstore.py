import random
from tests.api.clients.petstore_client import PetStoreClient
from tests.api.models.pet_model import Pet

def test_criar_buscar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet = Pet(
        id=random.randint(1000, 9999),
        name="Dog QA",
        status="available"
    )

    response_create = client.create_pet(pet)
    assert response_create.status == 200

    response_get = client.get_pet(pet.id)
    assert response_get.status == 200

    pet_response = Pet.from_response(response_get.json())

    assert pet_response.name == pet.name
    assert pet_response.status == pet.status


def test_atualizar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet = Pet(
        id=random.randint(1000, 9999),
        name="Initial",
        status="available"
    )

    # Criação
    client.create_pet(pet)

    # Atualização
    pet.name = "Updated"
    pet.status = "sold"

    response_update = client.update_pet(pet)

    assert response_update.status == 200

    pet_response = Pet.from_response(response_update.json())
    assert pet_response.status == "sold"
    assert pet_response.name == "Updated"


def test_deletar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet = Pet(
        id=random.randint(1000, 9999),
        name="Temp",
        status="available"
    )

    client.create_pet(pet)

    response_delete = client.delete_pet(pet.id)
    assert response_delete.status == 200

    response_get = client.get_pet(pet.id)
    assert response_get.status == 404
