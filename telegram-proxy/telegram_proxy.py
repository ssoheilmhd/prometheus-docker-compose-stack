from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Environment variables for configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
PROXY_URL = os.getenv('PROXY_URL')

@app.route('/forward', methods=['POST'])
def forward_to_telegram():
    data = request.json
    alerts = data.get('alerts', [])

    for alert in alerts:
        status = alert.get('status', '').upper()
        alertname = alert.get('labels', {}).get('alertname', '')
        summary = alert.get('annotations', {}).get('summary', '')
        description = alert.get('annotations', {}).get('description', '')
        instance = alert.get('labels', {}).get('instance', '')

        message = f"""
        *{status} - {alertname}*
        Host: `{instance}`
        {summary}
        {description}
        """

        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            proxies={"https": PROXY_URL} if PROXY_URL else None,
            json={
                "chat_id": CHAT_ID,
                "text": message.strip(),
                "parse_mode": "MarkdownV2",
                "disable_web_page_preview": True
            }
        )

    return jsonify({"status": "success"})
