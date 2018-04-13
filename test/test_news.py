import unittest
from apps.models import NewsTop


news = NewsTop

class NewsTopTest(unittest.TestCase):
    '''class to test the creation of an top headline news '''

    def setUp(self):
        self.news_top = news(254,'cnn','peter','kuja home','ashorta','url','image', 'publish')

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.news_top, NewsTop))

if __name__== '__main__':
    unittest.main()
