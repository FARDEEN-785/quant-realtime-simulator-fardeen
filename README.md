# 📈 Quant Trading Simulator

A simple real-time simulator that uses the MACD (Moving Average Convergence Divergence) strategy to generate trading signals and visualize buy/sell decisions on a stock chart. Built with Python using 
`yfinance`, `pandas`, and `matplotlib`.

---

## 🧠 What It Does

This script:
- Downloads historical stock data (default: AAPL)
- Calculates the MACD and Signal Line
- Generates **Buy** and **Sell** signals based on MACD crossover
- Plots the price chart with MACD indicator and signal points

---

## 📊 Example Output

> The script displays a dual-panel chart showing:
- The **price chart** with Buy/Sell markers
- The **MACD indicator chart** below it

---

## 🛠️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/quant-trading-simulator.git
cd quant-trading-simulator

Install the required packages
pip install yfinance matplotlib pandas

Run the simulator
python main.py
