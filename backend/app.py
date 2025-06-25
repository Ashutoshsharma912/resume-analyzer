from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    data = request.get_json()
    role = data.get('role')
    resume_text = data.get('resume_text')

    score = random.randint(50, 100)
    suggestions = [
        f"Add more {role}-related keywords.",
        "Quantify your achievements (e.g., 'Increased engagement by 30%').",
        "Use clean formatting and structure for better ATS compatibility."
    ]

    return jsonify({
        'score': score,
        'suggestions': suggestions
    })

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
