# Stock portfolio tracker by Avishkar bhosale

import csv
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Hardcoded stock price dictionary (mock prices)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 3600
}

def print_header():
    print(Fore.CYAN + Style.BRIGHT + "📈 Welcome to the Stock Portfolio Tracker")
    print(Fore.YELLOW + "Enter the stock symbol and quantity you own.")
    print("Available stocks: " + ', '.join(STOCK_PRICES.keys()) + "\n")

def get_user_portfolio():
    portfolio = {}
    while True:
        stock = input(Fore.WHITE + "Enter stock symbol (or type 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(Fore.RED + f"❌ '{stock}' is not in our stock list. Try again.")
            continue

        try:
            qty = int(input(Fore.WHITE + f"Enter quantity of {stock}: "))
            if qty < 0:
                raise ValueError
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid positive integer for quantity.")
    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    print("\n" + Fore.GREEN + Style.BRIGHT + "📊 Portfolio Summary:")
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = qty * price
        total += investment
        print(Fore.BLUE + f"- {stock}: {qty} shares x ${price} = ${investment}")
    print(Fore.CYAN + Style.BRIGHT + f"\n💰 Total Investment Value: ${total}")
    return total

def save_to_file(portfolio, total):
    choice = input(Fore.YELLOW + "\nDo you want to save the summary? (y/n): ").lower()
    if choice != 'y':
        return

    format_choice = input("Save as .txt or .csv? (txt/csv): ").lower()
    if format_choice == 'txt':
        with open("portfolio_summary.txt", "w") as f:
            f.write("📊 Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                f.write(f"{stock}: {qty} shares x ${price} = ${qty * price}\n")
            f.write(f"\nTotal Investment: ${total}\n")
        print(Fore.GREEN + "✅ Saved to portfolio_summary.txt")

    elif format_choice == 'csv':
        with open("portfolio_summary.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, STOCK_PRICES[stock], qty * STOCK_PRICES[stock]])
            writer.writerow(["", "", "Total", total])
        print(Fore.GREEN + "✅ Saved to portfolio_summary.csv")
    else:
        print(Fore.RED + "❌ Invalid format. File not saved.")

def main():
    print_header()
    portfolio = get_user_portfolio()

    if not portfolio:
        print(Fore.RED + "⚠️ No stocks entered. Exiting.")
        return

    total = calculate_total_investment(portfolio)
    save_to_file(portfolio, total)

if __name__ == "__main__":
    main()
