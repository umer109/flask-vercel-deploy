from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(_name_)

fields_info = {
    "chemical_engineering": {
        "what_is": {
            "heading": "Who are Chemical Engineers & What they do?",
            "content": """A Chemical Engineer is a professional who applies the principles of chemistry, physics, mathematics, and engineering to solve problems involving the production or use of chemicals. Chemical Engineers work in a variety of industries, including:
- Pharmaceuticals
- Food and beverage
- Oil and gas
They are responsible for developing and implementing processes to manufacture chemicals, design and operate chemical plants, and ensure the safe handling of chemicals. Chemical Engineers must have a strong understanding of chemistry, physics, and mathematics, as well as the ability to work independently and as part of a team."""
        },
        "personality": {
            "heading": "Chemical Engineering as a career, is best for a person with these personalities",
            "content": """Top 3 personality traits for chemical engineers:
- Analytical: Chemical engineers need to be able to think critically and solve problems. They need to be able to understand and apply scientific principles to real-world problems.
- Detail-oriented: Chemical engineers need to be able to pay attention to detail and follow instructions carefully. They need to be able to identify and correct errors in their work.
- Teamwork: Chemical engineers often work in teams, so they need to be able to work well with others and communicate effectively.
Other beneficial traits include being organized, flexible, and having a strong work ethic."""
        },
        "scope": {
            "heading": "Chemical Engineering as a career is a good choice in Pakistan",
            "content": """1. High demand for chemical engineers: The chemical engineering field is growing rapidly, and there is a high demand for chemical engineers in a variety of industries.
2. Good salary: Chemical engineers typically earn a high salary, with a median annual wage of $109,120 in 2020. The top 10% of earners made more than $166,400 per year.
3. Opportunities for advancement: Chemical engineers have a lot of opportunities for advancement in their careers. They can move up to management positions, or they can start their own businesses.
4. Challenging and rewarding work: Chemical engineering is a challenging and rewarding field. Chemical engineers get to solve problems and develop new technologies that improve people's lives.
5. Diverse opportunities: Chemical engineers can work in a variety of industries, including:
- Pharmaceuticals
- Food and beverage
- Oil and gas"""
        },
        "related_careers": {
            "heading": "Few related careers to Chemical Engineer in Pakistan",
            "content": """1. Process Engineer: Design and optimize processes used to manufacture products.
2. Environmental Engineer: Design and implement solutions to environmental problems.
3. Biomedical Engineer: Develop medical devices and equipment.
4. Petroleum Engineer: Develop and improve methods for extracting oil and gas.
5. Industrial Engineer: Optimize production processes to improve efficiency.
These careers are all closely related to Chemical Engineering, and they all require similar skills and knowledge. However, they each have their own unique focus and set of responsibilities."""
        }
    },
    "artificial_intelligence": {
        "what_is": {
            "heading": "Who are Artificial Intelligence Engineers & What they do?",
            "content": """An Artificial Intelligence Engineer is a professional who develops and implements AI models and algorithms. AI Engineers work in a variety of sectors including:
- Technology
- Healthcare
- Finance
They are responsible for designing and building AI systems, ensuring they operate effectively, and integrating them into applications. AI Engineers need a strong background in computer science, mathematics, and engineering, and they must be proficient in programming and data analysis."""
        },
        "personality": {
            "heading": "Artificial Intelligence Engineering as a career, is best for a person with these personalities",
            "content": """Top 3 personality traits for AI engineers:
- Curiosity: AI engineers need to be naturally curious and interested in learning about new technologies and methodologies.
- Problem-solving: AI engineers need to have strong problem-solving skills to develop innovative solutions.
- Attention to detail: AI engineers need to pay attention to detail to ensure the accuracy and reliability of their AI models.
Additional traits include being adaptable, analytical, and having strong communication skills."""
        },
        "scope": {
            "heading": "Artificial Intelligence Engineering as a career is a good choice",
            "content": """1. Growing field: The field of artificial intelligence is expanding rapidly, with increasing demand for AI solutions across various industries.
- High earning potential: AI engineers often command high salaries due to the specialized nature of their work.
- Diverse opportunities: AI engineers can work in various domains such as machine learning, natural language processing, and robotics.
- Impactful work: AI engineers work on cutting-edge technologies that have the potential to transform industries and improve lives."""
        },
        "related_careers": {
            "heading": "Few related careers to Artificial Intelligence Engineering",
            "content": """1. Data Scientist: Analyze and interpret complex data to help companies make decisions.
2. Machine Learning Engineer: Develop algorithms that allow machines to learn from data.
3. Robotics Engineer: Design and build robotic systems.
4. Computer Vision Engineer: Develop systems that interpret visual data from the world.
5. NLP Engineer: Develop systems that process and analyze human language data.
These careers are closely related to AI engineering, each focusing on different aspects of data and algorithm development."""
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

if _name_ == '_main_':
    app.run(debug=True)
