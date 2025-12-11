from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("exit_poll_model.pkl", "rb"))

# Label mappings
mappings = {
    "gender": {"M":0, "F":1},
    "education": {"10th":0, "12th":1, "Graduate":2, "Postgraduate":3},
    "region": {"Urban":1, "Rural":0},
    "income": {"Low":0, "Medium":1, "High":2},
    "best_issue": {
        "unemployment":0,"inflation":1,"development":2,"corruption":3,
        "better_education":4,"strong_nation":5,"global_relations":6,
        "poverty_removal":7,"industrial_growth":8,"crime_control":9,
        "theft_issues":10,"farmer_issues":11,"healthcare_priority":12,
        "women_safety":13
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    gender = mappings["gender"][request.form["gender"]]
    education = mappings["education"][request.form["education"]]
    region = mappings["region"][request.form["region"]]
    income = mappings["income"][request.form["income"]]
    best_issue = mappings["best_issue"][request.form["best_issue"]]

    data = [[age, gender, education, region, income, best_issue]]
    pred = model.predict(data)[0]

# Convert numeric output → party name
    label_map = {0: "A", 1: "B", 2: "C"}
    party = label_map.get(pred, pred)

    return render_template("index.html", result=f"Predicted Party: {party}")

    # return render_template("index.html", result=f"Predicted Party: {pred}")

if __name__ == "__main__":
    app.run(debug=True)
