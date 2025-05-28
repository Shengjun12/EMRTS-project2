import json

# Step 1: Validate JSON format
def is_valid_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
        print("JSON is valid.")
        return True
    except Exception as e:
        print(f"JSON validation failed: {e}")
        return False

# Step 2: Stub - USPS address validation (placeholder)
def verify_address_usps(address):
    print(f"Verifying address (mock): {address}")
    return True

# Run validation
if __name__ == "__main__":
    input_file = "state_capitals.json"

    if is_valid_json(input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for state, info in data.items():
            verify_address_usps(info["address"])
    else:
        print("Please check your input JSON file.")
