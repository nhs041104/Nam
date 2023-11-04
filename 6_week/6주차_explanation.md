# TextRank

## 참고한 사이트 및 모듈
https://excelsior-cjh.tistory.com/93

```python
!pip install konlpy sumy requests beautifulsoup4
```
---

## 주요 코드 설명
```python
# 다음 뉴스 홈페이지 URL
news_url = 'https://news.daum.net/'
.
.
.
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
.
.
.
# 모든 뉴스 데이터를 하나의 리스트에 모으기
all_news_data = crawl_daum_news_home(news_url)

for article in all_news_data:
    title = article['title'].replace('\n', '').strip()
    article_url = article['link']
    article_content = crawl_daum_news_article(article_url)

    article['title'] = title
    article['link'] = article_url
    article['content'] = article_content.replace('\n', '').strip()
.
.
.
# TextRank를 사용하여 기사 내용 요약
    parser = PlaintextParser.from_string(article_content, Tokenizer("korean")) # 기사 내용을 한국어로 토큰화하고, 이를 TextRank 알고리즘에서 사용할 수 있는 형식으로 파싱, 이 파싱된 텍스트는 parser.document에 저장
    summarizer = TextRankSummarizer() # TextRankSummarizer()를 사용하여 TextRank 요약기 객체를 생성
    summary = summarizer(parser.document, sentences_count=2)  #  원하는 문장 수 만큼 요약 sentences_count 매개변수를 조정하여 원하는 문장 수를 설정
    # 요약 문장들을 summary 변수에 저장, 그 후 ' '.join(str(sentence) for sentence in summary)를 사용하여 요약된 각 문장을 하나의 텍스트 문자열로 합침
    article['summary'] = ' '.join(str(sentence) for sentence in summary)
```



