import random

import pytest
import requests

def test_one():
    response = requests.get("http://127.0.0.1:8000/test-api")
    response = response.json()
    testing_response = {
        "name": "testName",
        "count": 1,
        "priority": True
    }
    assert response == testing_response
    

def test_two():
    test_id = random.randrange(10)
    response = requests.post("http://127.0.0.1:8000/test-api/{test_id}".format(test_id=test_id),
                             data={"test": "auto", "log": True})
    response = response.json()
    testing_response = {
        "testId": test_id,
        "testType": "auto",
        "log": True
    }
    assert response == testing_response