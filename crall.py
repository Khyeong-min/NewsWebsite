import openpyxl
from newspaper import Article
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def JoongAng(JAlist, idNews):

    #중앙일보 Dataframe으로 만들 리스트 선언
    dfJANewsList = []
    dfJA_LDList = []

    #중앙일보 크롤링 시작
    for category in JAlist:  # 중앙일보 카테고리를 하나씩 대입
        html = urlopen("https://www.joongang.co.kr/" + category)  # 중앙일보에서 해당 카테고리 url
        bsObject = BeautifulSoup(html, "html.parser")  # url 화면을 html로 가져오기
        news0 = ''  # 기사 url이 3~4개 반복적으로 나오더라. 기사 당 한 번만 데이터를 긇어오려고 선언함

        for link in bsObject.find("ul", {"class": "story_list"}).find_all('a'):  # 카테고리 별 기사 url 가져오기
            newsNew = link.get('href')  # 개별 기사 url 저장됨

            if news0 != newsNew:  # 앞서 가져온 기사와 같은지 확인
                news0 = newsNew  # 다른 기사이므로 news0을 새로운 기사 url로 갱신

                a = Article(news0, keep_article_html=True, language='ko')  # newspaper3k 라이브러리 전용 html 로드

                # newspaper3k 라이브러리 전용~~~ 웹 파싱
                a.download()
                a.parse()

                article_html = a.article_html  # 기사 본문 html 코드 (기사 템플릿 html 파일에 넣을 코드?)
                title = a.title  # 기사 제목
                author = a.authors[0]  # 기사를 작성한 기자
                publish_date = a.publish_date  # 기사를 처음 업로드한 시간
                text = a.text  # 기사 본문 텍스트 정보만 (키워드 분석 전용 데이터)

                # -----------------------------------------------------------------------------
                # csv 로 데이터 저장하기 위한 리스트
                dfJANewsList.append([idNews, title, author, str(publish_date), article_html, text, JAlist[category], 'joongang'])

                # 데이터가 잘 저장되었는지 확인
                '''print(article_html)
                print('-------------------------------------------------------')
                print(title)
                print(author)
                print(publish_date)
                print(text)'''

                # --------------------------------------------------------------
                # 여기부터 호불호 데이터
                html_LD = urlopen(news0)  # 호불호 데이터 스크래핑을 위한 개별 뉴스 url 로드 (bs4 라이브러리 전용)
                bsObject_LD = BeautifulSoup(html_LD, "html.parser")  # bs4 라이브러리 전용 기사 전문 html 가져오기

                LDlist = []  # 호불호 데이터 저장을 위한 리스트

                # -------------------------------------------------------------------
                LD = bsObject_LD.find('div', {"class": "empathy_wrap"}).find_all('span', {"class": "count"})
                #print(LD)

                # 리스트 LD에 호불호 데이터 저장
                for i in LD:
                    LDlist.append(i.text)

                # --------------------------------------------------------------------
                # 호불호 데이터 csv 로 저장
                dfJA_LDList.append([idNews, LDlist[0], LDlist[1]])

                # 호불호 데이터가 잘 저장이 되었는지 확인
                #print(LDlist)

                # News 총 개수 저장
                idNews += 1

    #---------------------------------------------------------------------------------
    #뉴스, 호불호 Dataframe 만들기
    df_JANews = pd.DataFrame(dfJANewsList,
                             columns = ['idNews', 'Title', 'Author', 'PublishDate', 'BodyHTML', 'Text', 'Category', 'Newspaper'])
    df_JALD = pd.DataFrame(dfJA_LDList, columns = ['idNews', 'Likes', 'Dislikes'])

    #df_JANews['PublishDate'] = str(df_JANews['PublishDate'])

    #Dataframe 확인
    #print(df_JANews)
    #print(df_JALD)

    return df_JANews, df_JALD, idNews

def AJu(AJlist, idNews):

    #아주경제 Dataframe으로 만들 리스트 선언
    dfAJNewsList = []
    dfAJ_LDList = []

    #아주경제 크롤링 시작
    for category in AJlist:  # 아주경제 카테고리를 하나씩 대입
        for j in range(1, 5):
            html = urlopen("https://www.ajunews.com/" + category + "?page=" + str(j) + "&")  # 아주경제에서 해당 카테고리 url
            bsObject = BeautifulSoup(html, "html.parser")  # url 화면을 html로 가져오기
            news0 = ''  # 기사 url이 3~4개 반복적으로 나오더라. 기사 당 한 번만 데이터를 긇어오려고 선언함

            for link in bsObject.find("ul", {"class" : "news_list"}).find_all('a'):  # 카테고리 별 기사 url 가져오기
                newsNew = link.get('href')  # 개별 기사 url 저장됨
                #print(newsNew)
                if news0 != newsNew:  # 앞서 가져온 기사와 같은지 확인
                    news0 = newsNew  # 다른 기사이므로 news0을 새로운 기사 url로 갱신

                    a = Article("https:" + news0, keep_article_html=True, language='ko')  # newspaper3k 라이브러리 전용 html 로드

                    # newspaper3k 라이브러리 전용~~~
                    a.download()
                    a.parse()

                    article_html = a.article_html  # 기사 본문 html 코드 (기사 템플릿 html 파일에 넣을 코드?)
                    title = a.title  # 기사 제목
                    author = ''  # 기사를 작성한 기자
                    publish_date = a.publish_date  # 기사를 처음 업로드한 시간
                    text = a.text  # 기사 본문 텍스트 정보만 (키워드 분석 전용 데이터)

                    # -----------------------------------------------------------------------------
                    # csv 로 데이터 저장
                    dfAJNewsList.append([idNews, title, author, str(publish_date), article_html, text, AJlist[category], 'ajunews'])

                    # 데이터가 잘 저장되었는지 확인
                    '''print(article_html)
                    print('-------------------------------------------------------')
                    print(title)'''
                    #print(author)
                    '''print(publish_date)
                    print(text)'''

                    # --------------------------------------------------------------
                    # 여기부터 호불호 데이터
                    html_LD = urlopen("https:" + news0)  # 호불호 데이터 스크래핑을 위한 개별 뉴스 url 로드 (bs4 라이브러리 전용)
                    bsObject_LD = BeautifulSoup(html_LD, "html.parser")  # bs4 라이브러리 전용 기사 전문 html 가져오기

                    LDlist = []  # 호불호 데이터 저장을 위한 리스트

                    # -------------------------------------------------------------------
                    LD = bsObject_LD.find_all('em', {"id": "spanSum"})
                    # print(LD)

                    # 리스트 LD에 호불호 데이터 저장
                    for i in LD:
                        LDlist.append(i.text)

                    # --------------------------------------------------------------------
                    # 호불호 데이터 csv 로 저장
                    dfAJ_LDList.append([idNews, LDlist[0], LDlist[1]])

                    # 호불호 데이터가 잘 저장이 되었는지 확인
                    # print(LDlist)

                    #News 총 개수 저장
                    idNews += 1
    #-------------------------------------------------------------------------------------
    #뉴스, 호불호 Dataframe 만들기
    df_AJNews = pd.DataFrame(dfAJNewsList,
                               columns=['idNews', 'Title', 'Author', 'PublishDate', 'BodyHTML', 'Text', 'Category', 'Newspaper'])
    df_AJLD = pd.DataFrame(dfAJ_LDList, columns = ['idNews', 'Likes', 'Dislikes'])

    #df_AJNews['PublishDate'] = str(df_AJNews['PublishDate'])

    #Dataframe 상태 확인
    #print(df_AJNews)
    #print(df_AJLD)

    return df_AJNews, df_AJLD, idNews

def Dailian(DAILIlist, idNews):

    #데일리안 Dataframe으로 만들 list 선언
    dfDAILINewsList = []
    dfDAILI_LDList = []

    #데일리안 크롤링 시작
    for category in DAILIlist:  # 데일리안 카테고리를 하나씩 대입
        time.sleep(3)
        for j in range(1, 5):
            html = urlopen("https://www.dailian.co.kr/" + category + "?page=" + str(j))  # 데일리안에서 해당 카테고리 url
            bsObject = BeautifulSoup(html, "html.parser")  # url 화면을 html로 가져오기
            news0 = ''  # 기사 url이 3~4개 반복적으로 나오더라. 기사 당 한 번만 데이터를 긇어오려고 선언함

            for link in bsObject.find("div", {"class" : "itemContainer"}).find_all('a'):  # 카테고리 별 기사 url 가져오기
                newsNew = link.get('href')  # 개별 기사 url 저장됨
                #print(newsNew)
                if news0 != newsNew:  # 앞서 가져온 기사와 같은지 확인
                    news0 = newsNew  # 다른 기사이므로 news0을 새로운 기사 url로 갱신

                    a = Article("https://www.dailian.co.kr" + news0, keep_article_html=True, language='ko')  # newspaper3k 라이브러리 전용 html 로드

                    # newspaper3k 라이브러리 전용~~~
                    a.download()
                    a.parse()

                    article_html = a.article_html  # 기사 본문 html 코드 (기사 템플릿 html 파일에 넣을 코드?)
                    title = a.title  # 기사 제목
                    author = ''  # 기사를 작성한 기자
                    publish_date = a.publish_date  # 기사를 처음 업로드한 시간
                    text = a.text  # 기사 본문 텍스트 정보만 (키워드 분석 전용 데이터)

                    # -----------------------------------------------------------------------------
                    # csv 로 데이터 저장
                    dfDAILINewsList.append([idNews, title, author, str(publish_date), article_html, text, DAILIlist[category], 'dailian'])

                    # 데이터가 잘 저장되었는지 확인
                    '''print(article_html)
                    print('-------------------------------------------------------')
                    print(title)
                    print(author)
                    print(publish_date)
                    print(text)'''

                    # --------------------------------------------------------------
                    # 여기부터 호불호 데이터
                    html_LD = urlopen("https://www.dailian.co.kr" + news0)  # 호불호 데이터 스크래핑을 위한 개별 뉴스 url 로드 (bs4 라이브러리 전용)
                    bsObject_LD = BeautifulSoup(html_LD, "html.parser")  # bs4 라이브러리 전용 기사 전문 html 가져오기

                    LDlist = []  # 호불호 데이터 저장을 위한 리스트

                    # -------------------------------------------------------------------
                    # 리스트 LD에 호불호 데이터 저장
                    LD_like = bsObject_LD.find('span', {"id" : "news_likes"}).text
                    LD_dislike = bsObject_LD.find('span', {"id" : "news_hates"}).text
                    #print([LD_like, LD_dislike])
                    # --------------------------------------------------------------------

                    # 호불호 데이터 csv 로 저장
                    dfDAILI_LDList.append([idNews, LD_like, LD_dislike])

                    # 호불호 데이터가 잘 저장이 되었는지 확인
                    # print(LDlist)

                    #News 총 개수 저장
                    idNews += 1
    #-------------------------------------------------------------------------------------
    #뉴스, 호불호 Dataframe 만들기
    df_DAILINews = pd.DataFrame(dfDAILINewsList,
                               columns=['idNews', 'Title', 'Author', 'PublishDate', 'BodyHTML', 'Text', 'Category', 'Newspaper'])
    df_DAILILD = pd.DataFrame(dfDAILI_LDList, columns = ['idNews', 'Likes', 'Dislikes'])

    #df_DAILINews['PublishDate'] = str(df_DAILINews['PublishDate'])
    #Dataframe 상태 확인
    #print(df_DAILINews)
    #print(df_DAILILD)

    return df_DAILINews, df_DAILILD, idNews

if __name__ == '__main__':
    #신문사 별 카테고리
    JAlist = {'politics' : 0, 'money' : 1, 'society' : 2, 'sports' : 3,
              'lifestyle' : 4, 'culture' : 5, 'world' : 6}
    AJlist = {'politics' : 0, 'economy' : 1, 'society' : 2, 'cultureentertainment/sports' : 3,
              'cultureentertainment/culture' : 4, 'cultureentertainment/entertainment' : 5}
    DAILIlist = {'politics' : 0, 'economy' : 1, 'society' : 2, 'sports' : 3,
                 'lifeCulture' : 4, 'entertainment' : 5, 'world' : 6}

    #idNews 및 크롤링한 뉴스 개수 확인
    idNews = 0

    #신문사별 기사, 호불호 크롤링 시작
    df_JANews, df_JALD, idNews = JoongAng(JAlist, idNews)
    time.sleep(5)
    df_AJNews, df_AJLD, idNews = AJu(AJlist, idNews)
    time.sleep(5)
    df_DAILINews, df_DAILILD, idNews = Dailian(DAILIlist, idNews)

    #------------------------------------------------------------------------------------------------------
    #Dataframe 합치기
    df_News = pd.concat([df_JANews, df_AJNews, df_DAILINews], ignore_index=True)
    df_LD = pd.concat([df_JALD, df_AJLD, df_DAILILD], ignore_index=True)

    #뉴스 dataframe 길이 확인
    shape = df_News.shape

    #합친 Dataframe 확인
    print(df_News)
    print(df_LD)

    #----------------------------------------------------------------------------------------------------
    #날짜순으로 정렬
    df_News = df_News.sort_values(by=["PublishDate"], ascending=[False])

    #기사 제목이 중복되는 행 삭제
    df_News = df_News.drop_duplicates(['Title'], keep='first')

    #----------------------------------------------------------------------------------------------------
    #Dataframe 저장
    df_News.to_csv('News.csv', encoding='utf-8')
    df_News.to_excel('News.xlsx', encoding='utf-8', sheet_name='News')

    df_LD.to_csv('LikeDislike.csv', encoding='utf-8')
    df_LD.to_excel('LikeDislike.xlsx', encoding='utf-8', sheet_name='LikeDislike')