
# Stock Price Tracker

A simple Flask-based web application to track the stock price of various companies using the MarketStack API. This application allows users to enter a stock symbol (e.g., AAPL) and retrieve the latest stock price along with other relevant information such as open price, close price, high, low, and the date of the data.

## Features
- **Stock Price Search**: Users can search for stock information by entering a stock symbol.
- **Stock Data Display**: Displays stock data such as open, close, high, and low prices.
- **User-friendly UI**: A responsive and clean interface built with Bootstrap.
- **Error Handling**: Displays error messages when no data is found or when there’s an issue with the API.

## Technologies Used
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, and Bootstrap for styling
- **API**: MarketStack API for real-time stock data
- **Dependencies**:
  - Flask
  - Requests

## Installation

### Prerequisites
Before running the project, ensure you have Python installed on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/Prathamesh326/Stock-Price-Tracker.git
```

### 2. Install dependencies
Navigate to the project directory and install the required dependencies using pip:
```bash
cd Stock-Price-Tracker
pip install -r requirements.txt
```

### 3. Set your MarketStack API key
Create a `.env` file in the root of the project and add your API key from MarketStack:
```plaintext
API_KEY=your_marketstack_api_key_here
```

### 4. Run the application
Run the Flask app:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the application.

## API Documentation
This application uses the MarketStack API to fetch stock data. To retrieve the stock data for a given symbol, the following API endpoint is used:
```
https://api.marketstack.com/v1/eod?access_key=your_api_key&symbols=symbol
```

### Example API Request
```python
import requests

url = "https://api.marketstack.com/v1/eod"
params = {
    "access_key": "your_api_key",
    "symbols": "AAPL"
}

response = requests.get(url, params=params)
print(response.json())
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **MarketStack API** for providing free access to stock data.
- **Bootstrap** for an easy-to-use framework for styling the app.

### Key Points:
1. **Overview**: It includes the purpose and features of the app.
2. **Technologies**: Lists the technologies used in the project.
3. **Installation Instructions**: Provides steps to clone the repo, install dependencies, and run the app.
4. **API Details**: Documents the API endpoint used for stock data fetching.
5. **License & Acknowledgments**: Adds a basic license section and credits any third-party services.
