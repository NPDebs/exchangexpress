import requests
from APP_ID import APP_ID as key

# request rates from API
def fetch_rates(key):
    base_url = "https://openexchangerates.org/api/latest.json?app_id={}".format(key)
    response = requests.get(base_url)

    return response.json()["rates"] if response.status_code == 200 else print("Couldn't fetch exchange rates. Status code:", response.status_code) 
    return None

