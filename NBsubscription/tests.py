#NBCrawler 대신 은서 파일 이름을 넣어주기만 하면 될 것 같아
from .views import NBsubscription
import unittest


class NBsubs_Test(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.subslist = [20, 30, 50]


    def tearDown(self):
        print("tearDown")


    def test_NBsubs(self):
        NBsubscription(self.subslist)
