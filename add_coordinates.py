import json
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Step 3: Add coordinates
def add_coordinates(data):
    geolocator = Nominatim(user_agent="emrts_capital_locator")

    for state, info in data.items():
        address = info["address"]
        attempts = 0
        max_retries = 3
        success = False

        while attempts < max_retries and not success:
            try:
                location = geolocator.geocode(address, timeout=10)
                if location:
                    info["latitude"] = location.latitude
                    info["longitude"] = location.longitude
                    print(f"[{state}] → {location.latitude}, {location.longitude}")
                    success = True
                else:
                    print(f"[WARNING] Could not geocode {state} ({address})")
                    break
            except (GeocoderTimedOut, GeocoderServiceError) as e:
                print(f"[RETRY {attempts+1}] {state}: {e}")
                attempts += 1
                time.sleep(2)
            except Exception as e:
                print(f"[ERROR] {state}: {e}")
                break

        time.sleep(1)  # avoid rate limiting

    return data

# Step 4: Validate coordinates
def validate_coordinates(data):
    for state, info in data.items():
        if not isinstance(info.get("latitude"), (float, int)) or not isinstance(info.get("longitude"), (float, int)):
            print(f"[INVALID COORD] {state}: Missing or invalid coordinates")
            return False
    return True

# Main execution
if __name__ == "__main__":
    input_file = "state_capitals.json"
    output_file = "state_capitals_with_coords.json"

    with open(input_file, "r", encoding="utf-8") as f:
        state_data = json.load(f)

    updated_data = add_coordinates(state_data)

    if validate_coordinates(updated_data):
        print("[✓] All coordinates validated.")
    else:
        print("[✗] Coordinate validation failed.")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(updated_data, f, indent=4, ensure_ascii=False)

    print(f"[✓] Output written to {output_file}")
