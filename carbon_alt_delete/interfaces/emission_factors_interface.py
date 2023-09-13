from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface


class EmissionFactorsInterface(ModelInterface):
    def grant_license(self, user_id: UUID | str):
        if isinstance(user_id, str):
            user_id = UUID(hex=user_id)
        url_stub = f"emission-factors/dataset/ecoinvent/license/{user_id}"

        return self.client.post(url_stub, {"userId": str(user_id)}).json()
