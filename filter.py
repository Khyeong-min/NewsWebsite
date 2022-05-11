import pandas as pd


def Filtering(df_comment):
    # 필터링 대상이 되는 단어 가져오기
    df_bad_words = open("bad_words.txt", "r", encoding="utf-8")

    # bad_words 확인
    for line in df_bad_words.readlines():
        # print(type(line))
        words = line.split(", ")
        # print(type(words))
        # print(words)

    # words 다시 한 번 확인
    # print(words)

    # bad_words가 댓글에 있으면 하트 이모티콘으로 바꾸기
    for word in words:

        # 'text' column 중 word 문자열이 포함된 것만 df_word dataframe으로 저장
        df_word = df_comment[df_comment['text'].str.contains(word)]
        # print(df_word)

        # df_word 행마다 반복해서 불러오기
        for idxcomment, text_word in df_word.iterrows():
            # 'text' 값을 str로 형변환
            text_word = str(text_word[2])

            # 변경 이전 값 확인
            # print(text_word)

            # 해당 word만 변경
            new_text = text_word.replace(word, '🤍❣🧡💛')

            # 변경 이후 값 확인
            # print(new_text)

            # 기존 df_comment에서 인덱스로 변경된 문자열 new_text로 값 변경경
            df_comment.at[idxcomment, 'text'] = new_text
            # print(df_comment.loc[idxcomment, 'text'], end='\n\n')

    # print(df_comment['text'])

    return df_comment


# comment 데이터 가져오기
df_comment = pd.read_excel("comment.xlsx", index_col=0)

# 필터링
df_comment = Filtering(df_comment)

# df_comment 파일로 저장
df_comment.to_csv('comment.csv', encoding='utf-8')
df_comment.to_excel('comment.xlsx', encoding='utf-8', sheet_name='comment')
