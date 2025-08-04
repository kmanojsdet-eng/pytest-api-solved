from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
@pytest.fixture
def new_order():
    # Create a new pet for the order
    pet_payload = {
        "id": 10,
        "name": "test_pet_for_order",
        "type": "dog",
        "status": "available"
    }
    api_helpers.post_api_data("/pets/", pet_payload)

    # Place an order for the new pet
    order_payload = {
        "pet_id": 10
    }
    response = api_helpers.post_api_data("/store/order", order_payload)

    order_id = response.json()['id']
    return order_id

def test_patch_order_by_id(new_order):
    order_id = new_order
    test_endpoint = f"/store/order/{order_id}"
    patch_payload = {
        "status": "sold"
    }

    response = api_helpers.patch_api_data(test_endpoint, patch_payload)

    assert response.status_code == 200
    assert response.json()['message'] == "Order and pet status updated successfully"

    # Optional: verify the pet's status is updated
    pet_response = api_helpers.get_api_data("/pets/10")
    assert pet_response.json()['status'] == 'sold'
