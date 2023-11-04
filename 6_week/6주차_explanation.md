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

## 출력결과

|    | title | link | content | summary |
|-------|-------|-------|-------|-------|
| 0 | 낙엽이 보호색?…가을 단풍철, 독사에 물렸을 때 대처하는 법| https://v.daum.net/v/20231104232630042 | ⓒ게티이미지뱅크 산림청에 따르면, 올해 단풍의 절정 시기는 10월 하순부터 11월 초다. ...... | 국내 국립공원에 서식하는 뱀은 유혈 목이, 살모사, 쇠 살모사, 까치 살모사, 누룩뱀, 구렁이, 능 구렁이, 대륙 유혈 목이, 비바리 뱀, 실뱀, 무자치 등 약 11 종이다. 또 한 뱀을 무리하게 포획하거나 독을 입으로 빨아내는 경우 더 큰 인명사고가 발생할 수 있으니 자제해야 한다. |
| 1 | "이스라엘군, 자발리아 난민촌 학교 공습…15명 사망·70명 부상" | https://v.daum.net/v/20231104225854919 | 4일(현지시간) 이스라엘군이 가자지구 북부 자발리아에서 난민 대피소로 사용되던 알파쿠라 학교를 공습해 다수의 인명피해가 발생했다. ...... | 4일( 현지시간) 이스라엘군이 가자지구 북부 자 발리아에서 난민 대피소로 사용되던 알파 쿠라 학교를 공습해 다수의 인명피해가 발생했다. ( 서울= 뉴스 1) 박 재하 기 자 = 이스라엘군이 가자지구에서 난민 대피시설로 사용되는 학교를 공습해 다수의 인명피해가 발생했다. |
| ... | ... | ... | ... | ... |
| 24 | "그냥 미미하게 살면 된다" 정보라 작가가 말하는 삶과 소설 |https://v.daum.net/v/20231104223503857 | [장슬기의 언더뷰] 작가 정보라[미디어오늘 장슬기 기자]“삶이 고통의 바다라서…” 지난 8월 장편소설 <고통에 관하여>를 출간한 정보라 작가는 고통에 천착하는 이유를 이렇게 설명했다. ...... |  미디어 오늘 장 슬기 기자] “ 삶이 고통의 바다라서…” 지난 8월 장편소설 < 고통에 관하여 >를 출간한 정보라 작가는 고통에 천착하는 이유를 이렇게 설명했다. 살아 있는 이들 만 고통을 느낄 수 있기에 고통은 삶과 죽음을 구별하는 기준 이자 삶의 본질인지도 모른다고 정보라 작가는 소설을 통해 이야기한다. |



