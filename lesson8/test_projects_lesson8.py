import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = "dCf8jSLWi1s8qFA2ckO7Ni-zSJxgmFcUY4bY9H3VDXUyPIG6yegwUIO3tpRGrycS"

@pytest.fixture
def create_project():
    return test_create_project_positive()

def test_create_project_positive():
    payload = {
        "title": "Проект урока 8",
        "users": {
          "a7192947-c350-46af-9912-a50d65236e7b": "admin"
        }
    }
    headers ={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.post(BASE_URL, json=payload, headers=headers)
    assert resp.status_code ==201
    resp_data = resp.json()
    project_id = resp_data["id"]
    return project_id

def test_create_project_negative():
    payload = {
        "title": "",
        "users": {
          "a7192947-c350-46af-9912-a50d65236e7b": "admin"
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.post(BASE_URL, json=payload, headers=headers)
    assert resp.status_code ==400

def test_editing_project_positive():
    project_id = create_project
    payload = {
        "deleted": False,
        "title": "Госуслуги",
        "users": {
          "a7192947-c350-46af-9912-a50d65236e7b": "admin"
        }
    }
    headers ={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.put(f"(BASE_URL)/{project_id}", json=payload, headers=headers)
    assert resp.status_code ==200

id_negative = "345dfhu689sdf123cvvbnm"

def test_editing_project_negative():
    payload = {
        "deleted": True,
        "title": "Госуслуги",
        "users": {
          "a7192947-c350-46af-9912-a50d65236e7b": "admin"
        }
    }
    headers ={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.put(f"(BASE_URL)/{id_negative}", json=payload, headers=headers)
    assert resp.status_code == 404

def test_id_project_positive():
    project_id = create_project

    headers ={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.get(f"(BASE_URL)/{project_id}", headers=headers)
    assert resp.status_code ==200

def test_id_project_negative():

    headers ={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.get(f"(BASE_URL)/{id_negative}", headers=headers)
    assert resp.status_code == 404
