import app
import json
from src.db import get_db

def test_get_all_task(app, client):
  with app.app_context():
    db = get_db()
    db.execute("INSERT INTO task(name, status) VALUES('task 1', 0)")
    db.dispose()

  response = client.get("/tasks")
  assert response.status_code == 200

  res_dict = json.loads(response.data.decode('utf-8'))
  assert len(res_dict['result']) == 1
  assert res_dict['result'][0]['name'] == 'task 1'
  assert res_dict['result'][0]['status'] == False

def test_put_task(app, client):
  with app.app_context():
    db = get_db()
    db.execute("INSERT INTO task(id, name, status) VALUES(111, 'task 1', 0)")
    db.dispose()

  response = client.put("/task/111", data={"id": 111, "name": "updated task", "status": 1})

  with app.app_context():
    db = get_db()
    result = db.execute(f"SELECT * FROM task WHERE id = '111'").fetchone()
    db.dispose()
    assert result['name'] == "updated task"
    assert result['status'] == 1

  assert response.status_code == 200

def test_create_task(app, client):
  response = client.post("/task", data={"name": "new task", "status": 1})
  res_dict = json.loads(response.data.decode('utf-8'))

  task_id = res_dict['result']['id']

  with app.app_context():
    db = get_db()
    result = db.execute(f"SELECT * FROM task WHERE id = '{task_id}'").fetchone()
    db.dispose()
    assert result['name'] == "new task"
    assert result['status'] == 0

  assert response.status_code == 201

def test_delete_task(app, client):
  with app.app_context():
    db = get_db()
    db.execute("INSERT INTO task(id, name, status) VALUES(111, 'task 1', 0)")
    db.dispose()

  response = client.delete("/task/111")
  assert response.status_code == 200
  
  with app.app_context():
    db = get_db()
    result = db.execute("SELECT * FROM task WHERE id = '111'").fetchone()
    db.dispose()
    assert result == None
    
