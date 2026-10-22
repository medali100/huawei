import os
from flask import Flask, jsonify
from flask_cors import CORS  # مكتبة السماح بالاتصال الخارجي
import requests

app = Flask(__name__)
CORS(app)  # تفعيل الميزة لجميع الروابط والتطبيقات

MODEM_IP = "192.168.100.1"
USERNAME = "telecomadmin"
PASSWORD = "hafsibayouta123"

@app.route('/')
def home():
    return jsonify({"status": "online", "message": "Server is running perfectly! 🚀"})

@app.route('/reboot', methods=['GET'])
def reboot_modem():
    try:
        return jsonify({"status": "success", "message": "Reboot command sent to Huawei modem! ⏳"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

  
