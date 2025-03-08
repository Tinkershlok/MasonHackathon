from flask import Flask, render_template, requests, url_for, redirect
import requests
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
