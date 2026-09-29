# CODE_RUNNER: 3.14 Flask routes
from flask import Flask, jsonify
import json

app = Flask("uesl_homework", root_path="/")

@app.route("/score")
def score():
    return jsonify({"home": 6, "away": 4, "period": 2})

@app.route("/roster")
def roster():
    return jsonify({"players": ["Adhvay", "Ishan", "Rohan"]})

@app.route("/record")
def record():
    return jsonify({"team": "UESL Practice Team", "wins": 3, "losses": 1})

client = app.test_client()
for path in ["/score", "/roster", "/record"]:
    response = client.get(path)
    assert response.status_code == 200
    print(path + ":", json.dumps(response.get_json(), sort_keys=True))
assert client.get("/missing").status_code == 404
print("Unknown route correctly returns 404")
