from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

fields_info = {
    "Engineering": {
        "scope": {
            "heading": "Scope of Engineering",
            "content": "Engineering is a broad field with applications in many industries. It offers various career paths including civil, mechanical, electrical, and software engineering."
        },
        "career": {
            "heading": "Career Paths in Engineering",
            "content": "Career options in engineering include roles like Design Engineer, Project Manager, Research Engineer, and more."
        },
        "skills": {
            "heading": "Skills Required for Engineering",
            "content": "Key skills include problem-solving, analytical thinking, proficiency in mathematics and sciences, and technical expertise."
        }
    },
    "Medicine": {
        "scope": {
            "heading": "Scope of Medicine",
            "content": "Medicine involves the study and practice of diagnosing, treating, and preventing illnesses. It encompasses various specialties such as surgery, general practice, and pediatrics."
        },
        "career": {
            "heading": "Career Paths in Medicine",
            "content": "Medical careers include roles such as General Practitioner, Surgeon, Specialist Doctor, and Medical Researcher."
        },
        "skills": {
            "heading": "Skills Required for Medicine",
            "content": "Important skills include attention to detail, empathy, communication skills, and strong foundational knowledge in medical sciences."
        }
    },
    "Computer Science": {
        "scope": {
            "heading": "Scope of Computer Science",
            "content": "Computer Science covers the study of computers and computational systems. It includes theoretical studies and practical applications in software development, systems design, and more."
        },
        "career": {
            "heading": "Career Paths in Computer Science",
            "content": "Careers in computer science include Software Developer, Systems Analyst, Data Scientist, and Cybersecurity Specialist."
        },
        "skills": {
            "heading": "Skills Required for Computer Science",
            "content": "Essential skills are programming, algorithm design, problem-solving, and knowledge of various software and hardware systems."
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info', methods=['POST'])
def get_info():
    data = request.json
    field = data['field']
    parameter = data['parameter']
    info = fields_info.get(field, {}).get(parameter, {"heading": "Not found", "content": "No information available."})
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
