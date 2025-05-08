def stock_triage_system():
    print("=== Stock Market Triage Assistant ===")
    print("Welcome to the Trading Decision Expert System\n")

    stock = input("Enter Stock Symbol (e.g., AAPL): ").upper()
    current_price = float(input("Enter Current Price: "))
    ma_50 = float(input("Enter 50-day Moving Average: "))
    ma_200 = float(input("Enter 200-day Moving Average: "))
    rsi = float(input("Enter RSI (Relative Strength Index): "))
    volume = int(input("Enter Today's Trading Volume: "))
    avg_volume = int(input("Enter Average Daily Trading Volume: "))

    print("\nAnalyzing stock data...\n")

    # Initialize recommendation and reason
    recommendation = "Hold"
    reason = []

    # Rule Set
    if current_price > ma_50 > ma_200:
        recommendation = "Buy"
        reason.append("Bullish trend: Price above 50 & 200-day MA.")
    elif current_price < ma_50 < ma_200:
        recommendation = "Sell"
        reason.append("Bearish trend: Price below 50 & 200-day MA.")
    else:
        reason.append("Neutral trend: No strong signal from moving averages.")

    if rsi < 30:
        recommendation = "Buy" if recommendation != "Sell" else recommendation
        reason.append("Oversold condition (RSI < 30).")
    elif rsi > 70:
        recommendation = "Sell" if recommendation != "Buy" else recommendation
        reason.append("Overbought condition (RSI > 70).")

    if volume > avg_volume * 1.5:
        reason.append("High volume detected: Strong market interest.")
    elif volume < avg_volume * 0.5:
        reason.append("Low volume detected: Weak market interest.")

    # Determine risk level
    if abs(rsi - 50) < 20 and volume > avg_volume:
        risk_level = "Low"
    elif (rsi < 25 or rsi > 75) and volume < avg_volume * 0.5:
        risk_level = "High"
    else:
        risk_level = "Medium"

    # Final Output
    print("=== Trading Recommendation ===")
    print(f"Stock: {stock}")
    print(f"Current Price: ${current_price:.2f}")
    print(f"Recommendation: {recommendation}")
    print(f"Risk Level: {risk_level}")
    print("\nReason(s):")
    for r in reason:
        print(f"- {r}")


# Run the system
if __name__ == "__main__":
    stock_triage_system()