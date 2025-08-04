test_pet.py
	•	Fixed schema validation bug in test_pet_schema (corrected pet name type).
	•	Extended test_find_by_status_200 to cover all statuses and validate response and schema.
	•	Added test_get_by_id_404 to check proper 404 handling for invalid pet IDs.
	•	test_store.py
	•	Added test_patch_order_by_id for PATCH endpoint with fixture for isolated test data.
	•	Added assertions for status updates and response validation.
	•	schemas.py
	•	Corrected pet schema (name: string).
	•	Added order schema for validation.
	•	Bugs Found (Not all fixed)
	•	Schema type bug (fixed).
	•	API error message f-string bug (not fixed, out of scope).
	•	Potential redundant logic in order update (not fixed, does not affect observable behavior).
