from flask import Flask, render_template, jsonify, request
from backend.estimate_cost import estimate_cost  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form-submit', methods=['POST'])
def form_submit():
    data = request.get_json()
    print("Data received:", data)
    daily_budget, fligth_price, estimated_cost = estimate_cost(data["origin"], data["destination"], data["month"], data["duration"], data["travelerType"])
    return jsonify({
        'destination': data["destination"],
        'origin': data["origin"],
        'month': data["month"],
        'duration': data["duration"],
        'travelerType': data["travelerType"],
        'dailyBudget': daily_budget,
        'flightPrice': fligth_price,
        'estimatedCost': estimated_cost
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
