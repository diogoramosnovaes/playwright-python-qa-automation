import random
from tests.api.clients.petstore_client import PetStoreClient

def test_criar_buscar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet_id = random.randint(1000, 9999)

    payload = {
        "id": pet_id,
        "name": "Dog QA",
        "status": "available"
    }

    response_create = client.create_pet(payload)
    assert response_create.status == 200

    response_get = client.get_pet(pet_id)
    assert response_get.status == 200
    assert response_get.json()["name"] == "Dog QA"

def test_atualizar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet_id = random.randint(1000, 9999)

    payload = {"id": pet_id, "name": "Initial", "status": "available"}
    client.create_pet(payload)

    update_payload = {"id": pet_id, "name": "Updated", "status": "sold"}
    response_update = client.update_pet(update_payload)

    assert response_update.status == 200
    assert response_update.json()["status"] == "sold"

def test_deletar_pet(api_request_context):
    client = PetStoreClient(api_request_context)

    pet_id = random.randint(1000, 9999)
    client.create_pet({"id": pet_id, "name": "Temp", "status": "available"})

    response_delete = client.delete_pet(pet_id)
    assert response_delete.status == 200

    response_get = client.get_pet(pet_id)
    assert response_get.status == 404

