from flask import Flask, request
import requests
import os

app = Flask(__name__)

# البيانات من متغيرات البيئة
TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/webhook', methods=['POST'])
def webhook():
    # استلام البيانات من TradingView
    data = request.get_json()
    
    # تجهيز الرسالة
    msg = f"""
🚨 إشارة جديدة!
الزوج: {data.get('symbol')}
النوع: {data.get('action')}
السعر: {data.get('price')}
"""
    
    # إرسال لـ Telegram
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })
    
    return "تم الإرسال!"

if __name__ == '__main__':
    app.run()

