# test_task_tracker.py
from task_tracker import add_task, list_tasks, complete_task, tasks

def test_add_and_list():
    # start from a clean in-memory state for this test
    tasks.clear()
    add_task("Learn Git")
    add_task("Write tests")
    all_tasks = list_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0]["task"] == "Learn Git"
    assert all_tasks[0]["done"] is False

def test_complete():
    tasks.clear()
    add_task("Mark me done")
    complete_task(1)
    assert list_tasks()[0]["done"] is True
