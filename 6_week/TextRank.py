import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import pandas as pd

# 다음 뉴스 홈페이지 URL
news_url = 'https://news.daum.net/'

# 뉴스 페이지 불러오기
def crawl_daum_news_home(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("페이지를 찾지 못했습니다..ㅜ")
        return
    soup = BeautifulSoup(response.content, 'html.parser')

    # 뉴스 제목, 링크 불러오기
    news_articles = []
    article_tags = soup.find_all('strong', class_='tit_g')
    for tag in article_tags:
        article_title = tag.get_text().strip()
        article_link = tag.a['href']

        article = {
            'title': article_title,
            'link': article_link
        }
        news_articles.append(article)

    return news_articles

# 뉴스 기사 불러오기
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

# 모든 뉴스 데이터를 하나의 리스트에 모은 후 pandas로 출력
all_news_data = crawl_daum_news_home(news_url)

for article in all_news_data:
    title = article['title'].replace('\n', '').strip()
    article_url = article['link']
    article_content = crawl_daum_news_article(article_url)

    article['title'] = title
    article['link'] = article_url
    article['content'] = article_content.replace('\n', '').strip()

    # TextRank를 사용하여 기사 내용 요약
    parser = PlaintextParser.from_string(article_content, Tokenizer("korean"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentences_count=2)

    article['summary'] = ' '.join(str(sentence) for sentence in summary)

# 데이터프레임 생성
file = pd.DataFrame(all_news_data)
file
