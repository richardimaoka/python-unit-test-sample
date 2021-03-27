"""Test the Task data type"""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
  """Check .field functionality of namedtuple."""
  t = Task('buy milk', 'brain')
  assert t.summary == 'buy milk'
  assert t.owner == 'brain'
  assert (t.done, t.id) == (False, None)

## not a test function, as it doesn't follow the naming convention of test_xxx
def wazzup():
  assert 1 == 2