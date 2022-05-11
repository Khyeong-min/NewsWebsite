import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def NBsubscription(NBsubscriptionL):
    # 신문사 이름과 구독자 수를 저장하는 csv 파일 만들기
    df = pd.DataFrame({'newspaper': ['아주경제', '중앙일보', '데일리안'], 'preferVal': NBsubscriptionL})
    df.to_csv('NBsubscription.csv', index=True, encoding='UTF-8')

    # 모든 신문사의 구독자 수 총합
    total_prefer = df['preferVal'].sum()

    percent = []
    # percent 계산
    for i in range(len(NBsubscriptionL)):
        percent.append(NBsubscriptionL[i] / total_prefer * 100)

    # csv에 percent column 추가
    df['percent'] = percent

    # percent 최댓값을 추출하고 해당 인덱스에 해당하는 신문사 이름까지 저장
    newspaper = df['newspaper']
    idmax = df['percent'].idxmax()
    NB_1st = newspaper[idmax]
    NBsubscription_1st = percent[idmax]

    # 1위 신문사 정보 csv 파일에 저장
    final_df = pd.DataFrame({'NB_1st': [NB_1st], 'NBsubscription_1st': [NBsubscription_1st]})
    final_df.to_csv('1st_NB.csv', index=True, encoding='UTF-8')

    return


#장고 실행하면 바로 함수 실행
if __name__ == '__main__':

    # 신문사마다 네이버에서 할당받은 id
    presses = ['011', '025', '119']

    # 구독자 수 int로 저장할 리스트
    subscribe_list = []

    for press in presses:
        # 웹 드라이버 선언
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(2)

        # visit url
        driver.get(f"https://media.naver.com/press/{press}")
        time.sleep(5)

        # 파싱
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 값 가져오기
        subscribe = soup.find("span", {"class": "press_subscribe_badge"}).find_all("em")

        # 결과 확인
        subscribe = subscribe[0].string

        # 리스트에 저장
        subscribe_list.append(int(subscribe))

        # driver 종료
        driver.close()

    # 크롤링한 값을 이용하여 함수 실행
    NBsubscription(subscribe_list)