import requests

def get_geolocation(api_key, search_string):
    base_url = "https://us1.locationiq.com/v1/search"

    params = {
        "key": api_key,
        "q": search_string,
        "format": "json"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data:
        result = {
            "place_id": data[0].get("place_id", ""),
            "lat": data[0].get("lat", ""),
            "lon": data[0].get("lon", ""),
            "display_name": data[0].get("display_name", "")
        }
        return result
    else:
        error_msg = data.get("error", "no error message") if isinstance(data, dict) else "no error message"
        print(f"Error: {response.status_code} - {error_msg}")
        return None


api_key = "pk.ffb527a24bb8ef49c5a39a11dda28866"
search_string = input("Enter the location: ")

result = get_geolocation(api_key, search_string)

if result:
    print("\nOutput:")
    for key, value in result.items():
        print(f"{key}: {value}")
