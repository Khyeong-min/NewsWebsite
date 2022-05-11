#main 대신 크롤러(합본) 코드 파일 이름만 적어주면 될 것 같아

from crall import JoongAng, AJu, Dailian
import unittest


class News_CrawlerTest(unittest.TestCase):
    def setUp(self):
            print("setUp")
            self.idNews = 0
            self.JAlist = {'politics': 0, 'money': 1}
            self.AJlist = {'politics': 0, 'economy': 1}
            self.DAlist = {'politics': 0, 'economy': 1}

        #finish
    def tearDown(self):
        print("tearDown")


        #JoongAng news data save
    def test_JAnews_crawler(self):
        df_jaNews, df_jaLD, idNews = JoongAng(self.JAlist, self.idNews)
        df_jaNews.info()
        self.assertEqual(df_jaNews.shape[0], idNews)
        self.assertEqual(df_jaLD.shape[0], idNews)



        #AJu news data save
    def test_AJnews_crawler(self):
        df_ajNews, df_ajLD, idNews = AJu(self.AJlist, self.idNews)
        df_ajNews.info()
        self.assertEqual(df_ajNews.shape[0], idNews)
        self.assertEqual(df_ajLD.shape[0], idNews)


        #Dailian news data save
    def test_DAnews_crawler(self):
        df_daNews, df_daLD, idNews = Dailian(self.DAlist, self.idNews)
        df_daNews.info()
        self.assertEqual(df_daNews.shape[0], idNews)
        self.assertEqual(df_daLD.shape[0], idNews)