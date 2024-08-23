import requests

# API configuration
API_KEY = '9efcb8985f8d7fdfadbc51d2'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

def get_exchange_rate(base_currency, target_currency):
    url = f"{BASE_URL}{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'conversion_rates' in data:
            rates = data['conversion_rates']
            if target_currency in rates:
                return rates[target_currency]
            else:
                print(f"Currency {target_currency} not found.")
                return None
        else:
            print("Failed to retrieve conversion rates.")
            return None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def convert_currency(amount, rate):
    return amount * rate

def main():
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input(f"Enter the amount in {base_currency}: "))

    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
