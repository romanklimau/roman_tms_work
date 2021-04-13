from api.api_checks import PetApi


def test_add_pet_update_his_name(get_data_to_add_pet, del_added_pet):
    new_pet = get_data_to_add_pet
    pet_page = PetApi()

    pet_page.add_new_pet_to_petstore(get_data_to_add_pet)

    id_pet = new_pet["id"]
    pet_page.check_pet_in_store(id_pet)

    pet_page.delete_pet(del_added_pet)

    pet_page.check_avalability_pet(id_pet)
