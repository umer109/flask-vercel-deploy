from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

fields = [
    "Engineering",
    "Medicine",
    "Computer Science",
    "Business",
    "Arts",
    "Law",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology"
]

@app.route('/')
def index():
    return render_template('index.html', fields=fields)

@app.route('/get_info', methods=['POST'])
def get_info():
    data = request.json
    field = data['field']
    parameter = data['parameter']
    
    prompt = f"Provide information about {parameter} for {field}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    
    content = response.choices[0].text.strip()
    
    return jsonify({
        "heading": f"{parameter.capitalize()} of {field}",
        "content": content
    })

if __name__ == '__main__':
    app.run(debug=True)
