import unittest

def booksearch():
  return ()

class BookSearchTest(unittest.TestCase):
  def test_booksearch(self):
    self.assertEqual((), booksearch())

if __name__ == '__main__':
  unittest.main()