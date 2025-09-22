import requests

def get_exchange_rates(base='USD'):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates']
    except requests.RequestException:
        print("❌ Error fetching exchange rates. Check your internet connection.")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("❌ Unsupported currency code.")
        print(f"Supported currencies are: {', '.join(sorted(rates.keys()))}")
        return None
    # Convert amount to base currency (USD), then to target currency
    amount_in_base = amount / rates[from_currency]
    converted_amount = amount_in_base * rates[to_currency]
    return converted_amount

def main():
    print("💱 Currency Converter")

    rates = get_exchange_rates()
    if not rates:
        return

    print("\nSupported currencies:", ', '.join(sorted(rates.keys())))

    while True:
        from_currency = input("Convert from (currency code, e.g. USD): ").upper()
        to_currency = input("Convert to (currency code, e.g. EUR): ").upper()

        if from_currency not in rates:
            print(f"❌ '{from_currency}' is not a supported currency code. Please try again.")
            continue
        if to_currency not in rates:
            print(f"❌ '{to_currency}' is not a supported currency code. Please try again.")
            continue

        break

    while True:
        try:
            amount = float(input("Amount to convert: "))
            if amount < 0:
                print("⚠️ Amount should be positive. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")

    result = convert_currency(amount, from_currency, to_currency, rates)
    if result is not None:
        print(f"\n{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
