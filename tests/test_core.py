import pathlib 
import unittest 
from tempfile import TemporaryDirectory 

THUMBNAIL_URL = ( 
  'http:// books.google.com/books/content',
  '?id=OgtBw76OY5EC&printsec=frontcover',
  '&img=1&zoom=1&edge=curl&source=gbs_api' 
)

class SaveThumbnailsTest(unittest.TestCase):
  def setUp(self): #一時ディレクトリを作成する
    self.tmp=TemporaryDirectory() 
    
  def tearDown(self):
     #一時ディレクトリを片付ける
     self.tmp.cleanup()
     
  def test_save_thumbnails(self): 
    from booksearch.core import Book 
    book = Book({'id': '', 'volumeInfo': { 
      'imageLinks': { 
        'thumbnail': THUMBNAIL_URL 
      }}}) 
    # 処理を実行し、ファイルが作成さることを確認する
    filename = book.save_thumbnails(self.tmp.name)[0]
    self.assertTrue(pathlib.Path(filename).exists())
