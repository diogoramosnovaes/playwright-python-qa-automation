class PetStoreClient:
    def __init__(self, api):
        self.api = api

    def create_pet(self, payload):
        return self.api.post("/v2/pet", data=payload)

    def get_pet(self, pet_id):
        return self.api.get(f"/v2/pet/{pet_id}")

    def update_pet(self, payload):
        return self.api.put("/v2/pet", data=payload)

    def delete_pet(self, pet_id):
        return self.api.delete(f"/v2/pet/{pet_id}")
