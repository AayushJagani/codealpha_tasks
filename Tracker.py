# Step 1: Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

total_investment = 0
portfolio = {}

print("📈 Simple Stock Tracker")
print("Available stocks:", list(stock_prices.keys()))

# Step 2: User input loop
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue
    
    quantity = int(input(f"Enter quantity for {stock}: "))
    
    # Store in portfolio
    portfolio[stock] = quantity
    
    # Calculate investment
    total_investment += stock_prices[stock] * quantity

# Step 3: Display results
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares - ${stock_prices[stock]} each")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Step 4 (Optional): Save to file
save = input("\nDo you want to save to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock},{qty},{stock_prices[stock]}\n")
        file.write(f"Total Investment: ${total_investment}")
    
    print("✅ Data saved to portfolio.txt")