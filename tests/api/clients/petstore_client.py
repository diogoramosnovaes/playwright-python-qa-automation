from tests.api.models.pet_model import Pet

class PetStoreClient:

    def __init__(self, api):
        self.api = api

    def create_pet(self, pet: Pet):
        return self.api.post("/v2/pet", data=pet.to_payload())

    def get_pet(self, pet_id: int):
        return self.api.get(f"/v2/pet/{pet_id}")

    def update_pet(self, pet: Pet):
        return self.api.put("/v2/pet", data=pet.to_payload())

    def delete_pet(self, pet_id: int):
        return self.api.delete(f"/v2/pet/{pet_id}")
