import requests

def get_conversion_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()  
        if target_currency in data["rates"]:
            return data["rates"][target_currency]
        else:
            print(f"Conversion rate for {target_currency} not available.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversion rate: {e}")
        return None


base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ").upper()
target_currency = input("Enter the target currency (e.g., USD, EUR, GBP): ").upper()

rate = get_conversion_rate(base_currency, target_currency)
if rate:
    amount = float(input("Enter the amount to convert: "))
    converted_amount = amount * rate
    print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
else:
    print("Could not retrieve conversion rate.")
