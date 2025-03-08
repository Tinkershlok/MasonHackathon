from flask import Flask, render_template, url_for, redirect, request, jsonify
from datetime import datetime
import genapi
import json
"""
import os
from google import generativeai
import google.generativeai as genai"
"""
from google import genai


app = Flask(__name__)

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')

    

@app.route("/newschecker", methods=["POST", "GET"])
def check_news():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    ai_response = genapi.getresponse(user_message)
    
    return jsonify({"ai_message": ai_response})
    return render_template('newschecker.html')

if __name__=="__main__":
    #app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000), debug=os.environ.get('FLASK_DEBUG', True))
    app.run(debug=True)