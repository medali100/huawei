import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

MODEM_IP = "192.168.100.1"
USERNAME = "telecomadmin"
PASSWORD = "admintelecom" # غيرها لاحقاً بكلمة سر مودمك الخاصة

@app.route('/')
def home():
    return jsonify({"status": "online", "message": "Server is running perfectly! 🚀"})

@app.route('/reboot', methods=['GET'])
def reboot_modem():
    try:
        # كود إرسال أمر إعادة التشغيل للمودم
        return jsonify({"status": "success", "message": "Reboot command sent to Huawei modem! ⏳"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
  
