from flask import Flask, render_template, url_for, redirect
from datetime import datetime
import json
import os
import genapi


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/newschecker', methods=['POST'])
def check_news():
    return render_template('main.html')

if __name__=="__main__":
    #app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000), debug=os.environ.get('FLASK_DEBUG', True))
    app.run(debug=True)
