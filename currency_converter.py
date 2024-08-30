import requests

def convert_currency(from_currency, to_currency, amount):
    try:
        # API endpoint
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

        # Fetch exchange rates
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["rates"][to_currency]
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            raise Exception(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception("Network error occurred") from e
    except KeyError:
        raise Exception(f"Invalid currency code. Please check the currency codes and try again.")

# Usage example
from_currency = str(input("Enter the currency you'd like to convert from: ")).upper()
to_currency = str(input("Enter the currency you'd like to convert to: ")).upper()
amount = float(input("Enter the amount: "))

try:
    result = convert_currency(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} = {result} {to_currency}")
except Exception as e:
    print(f"Error: {str(e)}")