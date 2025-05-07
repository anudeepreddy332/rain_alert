# 🌧️ Rain Alert

**Get a heads-up when it's about to rain!**

This Python app uses the **OpenWeatherMap API** to forecast rain and sends you an SMS alert via **Twilio** so you can bring your umbrella before heading out.
---

## 🚀 Features

- Fetches 3-hour interval weather forecasts using OpenWeatherMap  
- Analyzes weather condition codes to detect rain (`weather ID < 700`)  
- Sends an SMS alert to your phone using Twilio  
- Securely manages API keys using environment variables  
---

## 🔧 Setup

### 1. Clone the Repo  
```bash
git clone https://github.com/your-username/rain_alert.git
cd rain_alert
```

### 2. Create a Virtual Environment  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables  
```bash
export my_api_key=your_openweather_api_key
export my_account_sid=your_twilio_account_sid
export owm_auth_token=your_twilio_auth_token
```
*(You can also use a `.env` file with `python-dotenv` if preferred.)*

### 5. Run the Script  
```bash
python main.py
```
---
## 📦 Requirements
- Python 3.7+  
- `requests`  
- `twilio`  
- *(Optional)* `python-dotenv` for `.env` support
