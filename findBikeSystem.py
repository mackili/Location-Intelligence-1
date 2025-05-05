import requests
import json

baseurl = "https://api.nextbike.net/maps/nextbike-live.json?city="
system_name = "WRM nextbike Poland"


def __request__(cityId: int) -> dict:
    url = baseurl + str(cityId)
    try:
        response = requests.get(url)
        print(response.json())
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()
    return response.json()


def __find_system__() -> dict | None:
    i = 0
    while i < 1000:
        i += 1
        city = __request__(i)
        if len(city["countries"]) < 1:
            continue
        if city["countries"][0]["name"] == system_name:
            return city.countries[0]
        else:
            continue


wrm = __find_system__()
print(wrm)
