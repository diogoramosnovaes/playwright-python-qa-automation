class Pet:
    def __init__(self, id: int, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def to_payload(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status
        }

    @staticmethod
    def from_response(data: dict):
        return Pet(
            id=data.get("id"),
            name=data.get("name"),
            status=data.get("status")
        )
