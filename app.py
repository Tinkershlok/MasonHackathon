import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from google import genai

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=("AIzaSyCM4uL_WXs76v7-cIFfuyrCY_OUhhkkY6A"))

@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("main.html")

@app.route("/about.html", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/newschecker.html", methods=["GET", "POST"])
def news_check():
    return render_template("newschecker.html")

@app.route("/scrape", methods=["POST"])
def scrape_website():
    if request.method == "POST":
        url = request.form.get("url") 

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            page_title = soup.title.string if soup.title else "No title found"

            page_content = soup.get_text()

            bias_analysis = check_bias(page_content)

            return render_template("main.html", 
                                   page_title=page_title, 
                                   page_content=page_content[:300], 
                                   bias_analysis=bias_analysis, 
                                   url=url)
        except Exception as e:
            return f"Error fetching or parsing the website: {e}"

    return render_template("main.html")

def check_bias(content):

    try:
        prompt = f"Analyze the following content and explain if there is any bias present:\n\n{content}"
        
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        
        bias_analysis = response.text
        return bias_analysis
    except Exception as e:
        return f"Error with Gemini API: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5001), debug=True)