import unittest

def test_failing():
  assert(1, 2, 3) == (3, 2, 1)


class TestOne(unittest.TestCase):
  def test_one(self):
    self.assertEqual(1, 2)
