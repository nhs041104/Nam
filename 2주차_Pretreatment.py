import requests
from bs4 import BeautifulSoup
import re
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

news_url = 'https://news.daum.net/'


##### 뉴스 페이지 불러오기 #####

def crawl_daum_news_home(url, keyword=None):
    response = requests.get(url)
    if response.status_code != 200:
        print("페이지를 찾지 못했습니다..ㅜ")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    ##### 뉴스 제목, 링크 불러오기 #####
    news_articles = []
    article_tags = soup.find_all('strong', class_='tit_g')
    for tag in article_tags:
        article_title = tag.get_text().strip()
        article_link = tag.a['href']
        if keyword is None or keyword.lower() in article_title.lower():
            article = {
                'title': article_title,
                'link': article_link
            }
            news_articles.append(article)

    return news_articles


##### 뉴스 기사 불러오기 #####

def crawl_daum_news_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("기사를 불러오지 못했습니다...ㅜ")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    article_content = soup.find('div', class_='article_view')
    if article_content:
        content = article_content.get_text()
    else:
        content = "글이 없는 기사 입니다."

    return content



all_news_data = []

########3사용자로부터 검색할 키워드 입력 받기
find_keyword = input("검색할 키워드를 입력하세요: ")

news_data = crawl_daum_news_home(news_url, keyword=find_keyword)

for article in news_data:
    title = article['title'].replace('\n', '').strip()
    article_url = article['link']
    article_content = crawl_daum_news_article(article_url)

    all_news_data.append({
        'title': title,
        'link': article_url,
        'content': article_content.replace('\n', '').strip()
    })

################예시 텍스트 데이터
text_data = str(all_news_data)

################정규식을 사용하여 특수 문자 및 숫자 제거
text_data = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣\s]", "", text_data)

################형태소 분석을 위해 Konlpy 라이브러리의 Okt 클래스 사용
okt = Okt()
tokens = okt.nouns(text_data)

#############불용어 제외
stopwords = ["을", "를", "이", "가", "은", "는", "의"]
filtered_tokens = [word for word in tokens if word not in stopwords]

################단어 빈도수 카운트
word_counts = Counter(filtered_tokens)

wordcloud = WordCloud(font_path="/content/drive/MyDrive/Colab Notebooks/NanumGothic-ExtraBold.ttf", background_color='white').generate_from_frequencies(word_counts)

#####################워드 클라우드 시각화
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()