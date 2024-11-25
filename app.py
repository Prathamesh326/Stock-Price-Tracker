from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# MarketStack API Configuration
API_URL = "https://api.marketstack.com/v1/eod"
API_KEY = "YOUR_API_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol:
            params = {
                "access_key": API_KEY,
                "symbols": symbol
            }
            response = requests.get(API_URL, params=params)
            data = response.json()

            if "data" in data and len(data["data"]) > 0:
                stock_data = data["data"][0]
                return render_template("result.html", stock=stock_data)
            else:
                error = f"No data found for symbol '{symbol}'"
                return render_template("index.html", error=error)
    return render_template("index.html") 

if __name__ == "__main__":
    app.run(debug=True)
