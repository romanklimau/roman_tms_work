import requests


class PetApi:

    def __init__(self):
        self.url = "https://petstore.swagger.io/v2/pet"

    def add_new_pet_to_petstore(self, new_pet):
        response = requests.post(self.url, json=new_pet)
        assert response.status_code == 200, 'pet has not been added'

    def check_pet_in_store(self, pet_id):
        response = requests.get(self.url + "/" + str(pet_id))
        assert response.status_code == 200, 'not found pet'

    def delete_pet(self, pet_data):
        response = requests.delete(self.url + '/' + '5234781', json=pet_data)
        assert response.status_code == 200, 'not deleted pet'

    def check_avalability_pet(self, pet_id):
        response = requests.get(self.url + "/" + str(pet_id))
        assert response.status_code == 404, 'pet did not leave'
