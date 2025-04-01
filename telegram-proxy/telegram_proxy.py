from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Environment variables for configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
PROXY_URL = os.getenv('PROXY_URL')

app = Flask(__name__)
@app.route('/forward', methods=['POST'])
def forward_to_telegram():
    alert_data = request.json
    message = f"""
    *[{alert_data['status'].upper()}] {alert_data['commonLabels']['alertname']}*
    {alert_data['commonAnnotations']['summary']}
    """

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        proxies={"http": PROXY_URL, "https": PROXY_URL} if PROXY_URL else None,
        json={
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
    )
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
