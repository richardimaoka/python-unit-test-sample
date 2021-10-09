"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'], defaults=[None, None, False, None])
# Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task(None)
    print(t1)
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert t[0] == 'buy milk' # TypeError: tuple indices must be integers or slices, not str
    # assert t["summary"] == 'buy milk' # TypeError: tuple indices must be integers or slices, not str
    assert (t.done, t.id) == (False, None)
