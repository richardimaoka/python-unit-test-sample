import imghdr
import pathlib
from .api import get_data, get_json


class Book:
    """APIレスポンスのVolumeInfo要素に対応"""

    def __init__(self, item):
        self.id = item['id']
        volume_info = item['volumeInfo']
        for k, v in volume_info.items():
            setattr(self, str(k), v)

    def __repr__(self):
        return str(self.__dict__)

    def save_thumbnails(self, prefix):
        """サムネイル画像を保存する"""
        paths = []
        for kind, url in self.imageLinks.items():
            thumbnail = get_data(url)

            # judge the suffix from the image data
            ext = imghdr.what(None, h=thumbnail)

            # pathlib.Path can add a path by / operator
            base = pathlib.Path(prefix) / f'{self.id}_{kind}'
            filename = base.with_suffix(f'.(ext)')
            filename.write_bytes(thumbnail)
            paths.append(filename)
        return paths


def get_books(q, **params):
    """書籍検索を行う"""
    params['q'] = q
    data = get_json(params)
    return [Book(item) for item in data['items']]
