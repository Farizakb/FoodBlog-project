import requests
from app import app
from flask import jsonify,request



@app.route('/api/events', methods = ["POST"])
def events():
    body = request.json
    requests.post('http://127.0.0.1:5002/api/events',json=body)
    
    return jsonify(message = 'success')

