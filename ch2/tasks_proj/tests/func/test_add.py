"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task


def test_add_reutnrs_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN return task_id is not of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)
