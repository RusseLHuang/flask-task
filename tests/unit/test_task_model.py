from src.task.task_entity import Task

def test_new_task():
  task = Task("cook meat", 0)
  assert task.name == "cook meat"
  assert task.status == False