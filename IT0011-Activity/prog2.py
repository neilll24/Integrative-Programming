import csv
import os
import requests

CSV_URL = "https://raw.githubusercontent.com/neilll24/main/Integrative-Programming/IT0011-Activity/currency.csv"

def fetch_csv(file_path):
    """Fetches the CSV file if it is not already present locally."""
    print("Fetching currency exchange data...")
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()  # Handle HTTP errors
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("File successfully downloaded.")
    except requests.exceptions.RequestException as error:
        print(f"Failed to download the file: {error}")
        exit(1)

def get_exchange_rates(file_path):
    """Reads currency exchange rates from a CSV file and stores them in a dictionary."""
    exchange_rates = {}

    # Download the file if it does not exist
    if not os.path.exists(file_path):
        fetch_csv(file_path)

    with open(file_path, newline='', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            if len(row) < 3:
                continue  # Ignore incomplete rows
            
            currency_code = row[0].strip().upper()
            try:
                exchange_rates[currency_code] = float(row[2].strip())
            except ValueError:
                continue  # Ignore invalid values
                
    return exchange_rates

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get current script path
    file_path = os.path.join(script_directory, "currency.csv")  # Define full CSV path
    
    exchange_rates = get_exchange_rates(file_path)

    try:
        amount_usd = float(input("Enter the amount in US dollars: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return

    desired_currency = input("Enter the target currency code: ").strip().upper()

    if desired_currency not in exchange_rates:
        print(f"Currency '{desired_currency}' not found in the exchange rate data.")
        return

    converted_value = amount_usd * exchange_rates[desired_currency]

    print(f"\nUSD: {amount_usd}")
    print(f"{desired_currency}: {converted_value}")

if __name__ == '__main__':
    main()

