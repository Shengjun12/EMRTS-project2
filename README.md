# Project 2: State Capitals Geodata JSON

## Objective
Create a valid and complete JSON file that includes all U.S. state capitals with:
- Official address (street, city, state, zip)
- Verified formatting and structure
- Accurate geographical coordinates (latitude and longitude)

This dataset supports the larger Traveling Politician Problem and will serve as a reference for routing and geospatial validation.

## Project Steps

 Step 1: Create Initial JSON
- File: `state_capitals.json`
- Contains 50 U.S. state capitals with full mailing addresses

 Step 2: Verify JSON Format
- Script: `validate_input.py`
- Validates whether the JSON structure is syntactically correct
- Placeholder function added for USPS API verification

 Step 2.1: Address Verification 
- Investigate access requirements for USPS Web Tools API
- Plan to split address into street, city, state, and zip
- Mock function is included in code for future integration

 Step 3: Append Coordinates
- Script: `add_coordinates.py`
- Uses `geopy` and OpenStreetMap Nominatim API to geocode each address
- Adds `latitude` and `longitude` fields to each state

 Step 4: Validate Coordinates
- Ensures each capital has valid float/integer values for coordinates

 Step 5: Output Final JSON
- File: `state_capitals_with_coords.json`
- Used for mapping and travel path computation
- Validated and formatted


## File Structure

```
state_capitals.json                # Step 1 output
state_capitals_with_coords.json    # Final output with lat/long
add_coordinates.py                 # Step 3: coordinate geocoding
validate_input.py                  # Step 2: JSON & mock USPS validation
README.md                          # Documentation
```

## Dependencies

- Python 3.8+
- geopy


## Contact

Prepared by: Shengjun Niu  
GitHub: https://github.com/Shengjun12  
Email: sniu28@wisc.edu  
Internship: EMRTS, Summer 2025
