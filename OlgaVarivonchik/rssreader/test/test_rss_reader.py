"""Module with the functions for testing rss-reader"""
import copy
import unittest

from rss_reader import *
from news_work import *
from url_work import *
from output_work import *


class RSSReaderTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_1(self):
        fname = os.path.join(os.path.dirname(__file__), 'test_update.json')
        with open(fname) as f:
            news_all = json.load(f)
        original_copy = copy.deepcopy(news_all)
        fname = os.path.join(os.path.dirname(__file__), 'test_update_1.json')
        with open(fname) as f:
            news_upd = json.load(f)
        news_new = news_update(news_all, news_upd)
        self.assertEqual(original_copy, news_new, 'news_update incorrect work!')

    def test_update_2(self):
        fname = os.path.join(os.path.dirname(__file__), 'test_update.json')
        with open(fname) as f:
            news_all = json.load(f)
        original_copy = copy.deepcopy(news_all)
        fname = os.path.join(os.path.dirname(__file__), 'test_update_2.json')
        with open(fname) as f:
            news_upd = json.load(f)
        news_new = news_update(news_all, news_upd)
        self.assertNotEqual(original_copy, news_new, 'news_update incorrect work!')

    def test_news_from_url(self):
        file_name = os.path.join(os.path.dirname(__file__), 'test_news_from_url.txt')
        test = news_from_url('https://www.kommersant.ru/RSS/main.xml', 1, file_name)
        self.assertNotEqual(test, None, 'news_from_url incorrect work!')

    def test_news_from_storage(self):
        file_name = os.path.join(os.path.dirname(__file__), 'test_update.json')
        fname = os.path.join(os.path.dirname(__file__), 'test_update_3.json')
        with open(fname) as f:
            news_active = json.load(f)
        ttt = datetime.datetime.strptime('20211026', "%Y%m%d").date()
        test = news_from_storage('https://feeds.skynews.com/feeds/rss/world.xml', 1, ttt, file_name)
        self.assertEqual(test, news_active, 'news_from_storage incorrect work!')

    def test_connect_url_1(self):
        self.assertNotEqual(connect_url('https://google.com'), None, 'connect_url incorrect work!')

    def test_connect_url_2(self):
        self.assertEqual(connect_url('https://goog111le.com'), None, 'connect_url incorrect work!')

    def test_print_news_json(self):
        self.assertEqual(print_news_json({'1': 2}), None, 'connect_url incorrect work!')

    def test_print_news_text(self):
        fname = os.path.join(os.path.dirname(__file__), 'test_update_1.json')
        with open(fname) as f:
            news_active = json.load(f)
        self.assertEqual(print_news_text(news_active), None, 'connect_url incorrect work!')

    def test_print_news_pdf(self):
        file_name = os.path.join(os.path.dirname(__file__), 'test_print_news.pdf')
        fname = os.path.join(os.path.dirname(__file__), 'test_update_1.json')
        with open(fname) as f:
            news_active = json.load(f)
        self.assertEqual(print_news_pdf(news_active, file_name), None, 'print_news_pdf incorrect work!')


if __name__ == '__main__':
    print('test')
    unittest.main()
