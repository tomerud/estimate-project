from flask import Flask, render_template, jsonify, request
from utils import estimate_cost  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button-click', methods=['POST'])
def button_click():
    data = request.get_json()
    print("Data received:", data)
    return jsonify({'message': 'Button was clicked in the backend!', 'test': 'test'}), 200

@app.route('/form-submit', methods=['POST'])
def form_submit():
    data = request.get_json()
    print("Data received:", data)
    estimated_cost = estimate_cost(data["destination"], data["duration"], data["travelerType"])
    return jsonify({
        'destination': data["destination"],
        'duration': data["duration"],
        'travelerType': data["travelerType"],
        'estimatedCost': estimated_cost
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
