# exchangexpress
import requests
from APP_ID import APP_ID as key

# request rates from API
def fetch_rates(key):
    base_url = "https://openexchangerates.org/api/latest.json?app_id={}".format(key)
    response = requests.get(base_url)

    return response.json()["rates"] if response.status_code == 200 else print("Couldn't fetch exchange rates. Status code:", response.status_code) 
    return None

exchange_rates = fetch_rates(key)

# function to convert currency
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency and to_currency in exchange_rates:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Sorry. Your currency codes are invalid.")
        return None

# receive user input
if exchange_rates:    
    amount = float(input("Enter amount: "))
    from_currency = input("Enter currency you want to convert from: ").upper()
    to_currency = input("Enter currency you want to convert to: ").upper()

    final_output = convert_currency(amount, from_currency, to_currency, exchange_rates)

    if final_output is not None:
        print(f"{amount} {from_currency} is equal to {final_output:.2f} {to_currency}")


# to-do > "Naira == NGN"