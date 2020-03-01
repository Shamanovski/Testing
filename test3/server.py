from flask import Flask, app, request
import json

app = Flask(__name__)

@app.route("/test-api/", methods=["GET"])
@app.route("/test-api/<int:test_id>", methods=["POST"])
def test_api(test_id=None):
    response = {
        "name": "testName",
        "count": 1,
        "priority": True
    }

    if test_id is not None:
        response = {
            "testId": test_id,
            "testType": "auto",
            "log": True
        }

    return json.dumps(response)

app.run("127.0.0.1", 8000)
