import random
import pytest

@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_buscar_pets_por_status(api, status):
    """Testa busca de pets por status"""
    response = api.get(f"/v2/pet/findByStatus?status={status}")
    assert response.status == 200
    assert isinstance(response.json(), list)


def test_criar_pet(api):
    """Testa criação de um novo pet"""
    pet_data = {
        "id": random.randint(1000, 9999),
        "name": "Dog QA",
        "status": "available",
        "photoUrls": []
    }
    
    response = api.post("/v2/pet", data=pet_data)
    assert response.status == 200
    
    response_data = response.json()
    assert response_data["name"] == pet_data["name"]
    assert response_data["status"] == pet_data["status"]


def test_atualizar_pet(api):
    """Testa atualização de um pet"""
    pet_id = random.randint(1000, 9999)
    
    # Criar pet
    pet_data = {
        "id": pet_id,
        "name": "Initial Name",
        "status": "available",
        "photoUrls": []
    }
    api.post("/v2/pet", data=pet_data)
    
    # Atualizar pet
    pet_data["name"] = "Updated Name"
    pet_data["status"] = "sold"
    
    response = api.post("/v2/pet", data=pet_data)
    assert response.status == 200
    
    response_data = response.json()
    assert response_data["name"] == "Updated Name"
    assert response_data["status"] == "sold"


def test_deletar_pet(api):
    """Testa deleção de um pet"""
    pet_id = random.randint(1000, 9999)
    
    # Criar pet
    pet_data = {
        "id": pet_id,
        "name": "Temp Pet",
        "status": "available",
        "photoUrls": []
    }
    api.post("/v2/pet", data=pet_data)
    
    # Deletar pet
    response = api.delete(f"/v2/pet/{pet_id}")
    assert response.status == 200
