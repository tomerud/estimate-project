from flask import Flask, render_template, jsonify, request
from backend.estimate_cost import estimate_cost  
from backend.find_most_similar import find_most_similar

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

@app.route('/alternatives')
def alternatives():
    # pull every field from the query string
    origin        = request.args.get('origin', '')
    destination   = request.args.get('destination', '')
    duration      = request.args.get('duration', '')
    month         = request.args.get('month', '')
    travelerType  = request.args.get('travelerType', '')
    dailyBudget   = request.args.get('dailyBudget', '')
    flightPrice   = request.args.get('flightPrice', '')
    estimatedCost = request.args.get('estimatedCost', '')


    return render_template(
        'alternatives.html',
        origin=origin,
        destination=destination,
        duration=duration,
        month=month,
        travelerType=travelerType,
        dailyBudget=dailyBudget,
        flightPrice=flightPrice,
        estimatedCost=estimatedCost
    )

@app.route('/get_other_destinations', methods=['POST'])
def get_other_destinations():
    weight_dict = {"notAtAll": 0, "aBit": 0.5, "soSo": 1, "aLot": 2, "dealBreaker": 3}
    data = request.get_json()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Data received:", data)
    
    try:
        res = find_most_similar(
            data["destination"], 
            data["month"],
            data["origin"],  
            data["duration"],
            data["travelerType"], 
            data["estimatedCost"], 
            weight_dict[data["development"]],
            weight_dict[data["farAway"]],
            weight_dict[data["weather"]],
            weight_dict[data["culture"]]
        )
        print("res is: ", res)
        return jsonify({"status": "ok", "result": res})  # Return the result for debugging
    except Exception as e:
        print("Error in find_most_similar:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
