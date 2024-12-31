
import requests

def get_conversion_rate(base_currency, target_currency):
    """Fetch conversion rate from a public API."""
    api_url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{base_currency}"
    
    try:
      
        response = requests.get(api_url)
        response.raise_for_status()  
        
        data = response.json()
        
        
        if target_currency in data['conversion_rates']:
            conversion_rate = data['conversion_rates'][target_currency]
            return conversion_rate
        else:
            raise ValueError("Target currency not supported")
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError as ve:
        print(ve)
        return None

def convert_currency(amount, base_currency, target_currency):
    """Convert currency from base_currency to target_currency."""
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        return None
    
    conversion_rate = get_conversion_rate(base_currency, target_currency)
    
    if conversion_rate:
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        print("Error in fetching conversion rate. Please try again later.")
        return None

def main():
    print("Welcome to the Currency Converter App!")

    try:
       
        amount = float(input("Enter the amount to convert: "))
        base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ").upper()
        target_currency = input("Enter the target currency (e.g., USD, EUR, GBP): ").upper()

    
        result = convert_currency(amount, base_currency, target_currency)
        
        if result is not None:
            print(f"{amount} {base_currency} is equal to {result:.2f} {target_currency}")
        else:
            print("There was an issue with the conversion.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

if __name__ == "__main__":
    main()
