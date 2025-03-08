from flask import Flask, render_template, url_for, redirect, request, jsonify
from datetime import datetime
"""
import json
import os
from google import generativeai
import google.generativeai as genai
import genapi
"""

app = Flask(__name__)

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')

@app.route('/newschecker.html', methods=['POST','GET'])
def check_news():
    return render_template('newschecker.html')

if __name__=="__main__":
    #app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000), debug=os.environ.get('FLASK_DEBUG', True))
    app.run(debug=True)