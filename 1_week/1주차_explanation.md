# 지금까지 했던 Crawling
## 크롤링 목표 사이트
- 다음 뉴스
  - 다음 뉴스 홈에서 실시간으로 올라오는 인기 뉴스 가져오기
- 유튜브 인기 급상승 음악
  - 전세계 유튜브 음악중 인기 급상승 중인 음악 가져오기
- 유튜브 재생목록 가져오기
  - 본인이 원하는 유튜브 재생목록 불러오기

## 내가 사용한 crawling 기법
- Requests 모듈: requests 모듈은 웹 페이지에 HTTP 요청을 보내고 응답을 받기 위해 사용. get 메서드를 사용하여 웹 페이지의 HTML 내용을 가져옴.
- Beautiful Soup: Beautiful Soup는 웹 페이지의 HTML 또는 XML에서 데이터를 추출하는 파싱 라이브러리로 HTML을 구문 분석하고 원하는 데이터를 추출하는 데 사용함.
- 뉴스 홈 페이지 크롤링: crawl_daum_news_home 함수는 다음 뉴스 홈페이지를 크롤링하는 함수. 해당 페이지에서 뉴스 기사의 제목과 링크를 추출함. 이를 위해 requests를 사용하여 웹 페이지를 불러오고, 그 후 BeautifulSoup을 사용하여 HTML 내용을 파싱. 그 다음, find_all 메서드로 뉴스 기사 제목에 해당하는 HTML 요소를 찾아서 제목과 링크를 추출함.
- 뉴스 기사 페이지 크롤링: crawl_daum_news_article 함수는 개별 뉴스 기사 페이지를 크롤링하는 함수로 주어진 기사 URL로 HTTP 요청을 보내서 해당 기사 페이지의 HTML 내용을 가져오고, 이를 다시 BeautifulSoup을 사용하여 파싱. 그런 다음, find 메서드를 사용하여 기사 내용이 들어있는 HTML 요소를 찾아서 내용을 추출함.
- 데이터 저장: 크롤링한 데이터는 모든 뉴스 기사에 대한 정보를 포함하는 리스트인 all_news_data에 저장함. 이 리스트에는 각 기사의 제목, 링크, 및 내용이 포함되어 있음.
- Pandas를 사용한 데이터프레임 생성: pandas 라이브러리를 사용하여 데이터를 데이터프레임 형식으로 변환하고 출력. 데이터프레임은 데이터를 표 형식으로 표시하며, 이 경우에는 크롤링한 뉴스 기사의 정보를 쉽게 관리하고 분석할 수 있도록 함.

## 수정한 코드
# **1. 다음뉴스**
```python
for article in news_data:
  title = article['title'].replace('\n', '').strip()
  article_url = article['link']
  article_content = crawl_daum_news_article(article_url)

  all_news_data.append({
    'title': title,
    'link': article_url,
    'content': article_content.replace('\n', '').strip()
  })
```
다음 뉴스에서 기사를 가져올때 제목과 기사글에 공백, 줄 바꿈 등이 계속 발생하여 replace와 strip을 이용하여 필요없는 공백과 줄바꿈을 전부 지워서 보기편하게 바꿈.


```python
find_keyword = input("검색할 키워드를 입력하세요: ")
```
또한 input을 사용하여 원하는 단어를 입력하면 그 단어가 포함되어있는 기사들을 불러오게 수정하였다

---

# **2. 유튜브 인기 급상승 음악**
```python
from googleapiclient.discovery import build
```
```python
youtube = build('youtube', 'v3', developerKey=API_KEY)
```

다음 뉴스에서 긁어온것 처럼 HTML로 가져오려고 했으나 유튜브의 경우 크롤링 했을때 유튜브의 정보를 가져올수가 없어 직접 유튜브 API를 사용하여 가져오는 방법을 선택.

---

# **3. 유튜브 재생목록 가져오기**
```python
API_KEY = 'API_KEY 입력'

playlist_id = '재생목록 ID 입력'
```
원래는 이처럼 직접 코드에 자신의 API와 원하는 유튜브 재생목록 ID를 입력해야했지만 좀더 편하고 코드를 바꾸면서 크롤링하는 것이 아닌 input으로 직접 정보를 받게 수정.

```python
API_KEY = input("자신의 Youtube API KEY를 입력하세요: ")

playlist_id = input("YouTube 재생목록 코드를 입력하세요: ")
```

또한 유튜브의 영상 조회수를 가져오는 과정에서 일의 자리까지 전부 나와 가독성이 떨어졌지만 단위를 설정하는 코드를 추가하며 가독성을 높힘
```python
# 영상 조회수 가져오기
    video_statistics = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()

    view_count = int(video_statistics['items'][0]['statistics']['viewCount'])
```



```python
#수정 후
# 숫자를 만단위로 변환하는 함수 정의 추
def format_view_count(view_count):
    if view_count >= 100000000:
        return f"{view_count // 100000000}억"
    elif view_count >= 10000:
        return f"{view_count // 10000}만"
    else:
        return str(view_count)
```

---

# **4. 최종 완성**

다음 뉴스
| title |  link  | content |
|-------|--------|---------|
| 서울시립장사시설 추석 성묘 10만여명 몰릴 듯…안전대책 마련 | https://v.daum.net/v/20230908111511676 | 용미리 시립묘지 [서울시 제공. 재판매 및 DB 금지] (서울=연...|
| ... | ... | ... |

유튜브 인기급상승 음악
| Title | Video URL | Thumbnail URL |
|--------|--------|---------|
| KAROL G - MI EX TENÍA RAZÓN (Official Video) | https://www.youtube.com/watch?v=VBcs8DZxBGc | https://i.ytimg.com/vi/VBcs8DZxBGc/default.jpg |
| ... | ... | ... |

유튜브 재생목록
| Title | Video URL | Thumbnail URL | View Count |
|--------|--------|---------|--------|
| Blueming (Blueming) | https://www.youtube.com/watch?v=I0_ZXHzKysc | https://i.ytimg.com/vi/I0_ZXHzKysc/default.jpg | 1억 |
| ... | ... | ... | ... |
