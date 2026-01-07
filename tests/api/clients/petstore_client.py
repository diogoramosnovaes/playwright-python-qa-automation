from tests.api.models.pet_model import Pet

class PetStoreClient:

    def __init__(self, api):
        self.api = api

    async def create_pet(self, pet: Pet):
        return await self.api.post("/v2/pet", data=pet.to_payload())

    async def get_pet(self, pet_id: int):
        return await self.api.get(f"/v2/pet/{pet_id}")

    async def update_pet(self, pet: Pet):
        return await self.api.put("/v2/pet", data=pet.to_payload())

    async def delete_pet(self, pet_id: int):
        return await self.api.delete(f"/v2/pet/{pet_id}")
