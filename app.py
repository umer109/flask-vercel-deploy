# app.py
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import openai
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

fields = [
    'Chemical Engineering',
    'Artificial Intelligence',
    'Data Science',
    # Add more fields as needed
]

@app.route('/fields', methods=['GET'])
def get_fields():
    return jsonify({'fields': fields})

def generate_content(field, parameter):
    prompt = f"Provide detailed information about {parameter.replace('_', ' ')} for the field of {field}."
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/<field>/<parameter>', methods=['GET'])
def get_field_details(field, parameter):
    try:
        content = generate_content(field, parameter)
        return jsonify({'heading': f'{parameter.replace("_", " ").capitalize()} for {field}', 'content': content})
    except Exception as e:
        return jsonify({'heading': 'Error', 'content': str(e)}), 500

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
