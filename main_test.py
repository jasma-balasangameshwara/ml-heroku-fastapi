import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def home():
    homeq = TestClient(app)
    return homeq


def test_index(home):
    connect = home.get("/")
    assert connect.status_code == 200
    assert connect.json() == ["Welcome Success"]


def test_predict_salary_1(home):
    data = {
        "age": 39,
        "workclass": "State-gov",
        "education": "Bachelors",
        "marital_status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "hours_per_week": 40,
        "native_country": "United-States"
    }
    connect = home.post('/', json=data)
    assert connect.status_code == 200
    assert connect.json() == {"income": " <=50K"}


def test_predict_salary_2(home):
    data = {
        "age": 560,
        "workclass": "Local-gov",
        "education": "Bachelors",
        "marital_status": "Married-civ-spouse",
        "occupation": "Tech-support",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "hours_per_week": 40,
        "native_country": "United-States"
    }
    connect = home.post('/', json=data)
    assert connect.status_code == 200
    assert connect.json() == {"income": " >50K"}
