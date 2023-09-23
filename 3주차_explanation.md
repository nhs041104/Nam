# 3주차 노래 가사 텍스트 파일 색인&검색
## 목표
- 파일에 있는 노래 가사 불용어 제거
- 파일에 원하는 단어 검색
- 해당 단어가 들어간 파일 불러와서 출력하기기

```python
import os
import re
import pandas pd
```
os 모듈과 re 모듈, pandas을 가져온다. os 모듈은 운영 체제와 상호 작용하는 데 사용되고 re 모듈은 정규 표현식을 사용하여 문자열을 처리하는 데 사용된다. 그리고 pandas를 이용해 결물을 깔끔하게 출력한다.

```python
data_folder = "/content/drive/MyDrive/Colab Notebooks/SING"
```
검색 대상이 될 폴더 경로를 변수 data_folder에 저장한다. 이 코드에서는 Google Colab 환경에서 /content/drive/MyDrive/Colab Notebooks/SING 경로를 사용했다.

```python
search_word = input("검색할 단어를 입력하세요: ")

file_info_list = []
```
검색할 단어를 입력하고 pandas를 출력할떄 필요한 리스트를 생성해준

```python
for root, dirs, files in os.walk(data_folder):
    for file in files:
        file_path = os.path.join(root, file)
```
os.walk() 함수를 사용하여 data_folder 경로 아래의 모든 파일과 디렉토리를 순회하는 루프를 건다. root는 현재 디렉토리의 경로를 나타내고, dirs는 현재 디렉토리 내의 하위 디렉토리를 나타낸다. files는 현재 디렉토리 내의 파일 목록을 나타낸다. 그리고 현재 디렉토리 내의 각 파일에 대한 루프를 시작하고 현재 파일의 경로를 file_path 변수에 저장한다. os.path.join() 함수는 디렉토리 경로와 파일 이름을 결합하여 완전한 파일 경로를 생성한다.

```python
with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
```
파일을 읽기 모드("r")로 열고 encoding="utf-8"은 파일을 UTF-8 인코딩으로 열도록 지정해준다. 그리고 파일 내용을 읽어와 file_content 변수에 저장한다.

```python
cleaned_content = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣\sA-Za-z]", "", file_content)
```
정규 표현식을 사용하여 파일 내용에서 한글, 공백, 영어 (A-Z 및 a-z)를 제외한 모든 문자를 제거하고, 결과를 cleaned_content 변수에 저장한다.


```python
if search_word in cleaned_content:
    file_info_list.append({"파일 이름": file, "본문 내용": cleaned_content})
```
이 부분은 검색어인 search_word가 파일 내용(cleaned_content)에 포함되어 있는지 확인하고, 포함되어 있다면 파일 정보를 file_info_list라는 리스트에 추가하는 역할을 한다.

```python
df = pd.DataFrame(file_info_list)
df
```
마지막으로 pandas를 이용해 결과물을 출력한다.


# 출력 결과
## 검색 단어 "사랑"

| ... | 파일 이름 | 가사 |
|-------|--------|---------|
| 0 | AKMU.txt | Why baby 뭐가문제야 baby Woah Woah Woah woah Hey woah Woah Anyone please Woah Woah woah 제발 사랑 좀 줘요 네가 날 싫어해 하는 걸 알아 나는 서운해 그런 날 왜 너는 못 이해해 You dont understand 난 너를 좋아한다고 내가 뭘 잘못했는데 내게 왜 그러는데 그럴수록 난 되게 섭섭해 Oh Im so sad 그러니까 슬슬 Let me come into your 마음 중요한 건 마음 결코 네 얼굴만 보고 좋아하는 거 아니 아니야 날 미워하는 너의 날이 선 말투까지도 사랑하게 된 거 이게 내 맘이야 너에 대한 건 사소한 것도 기억해 난 마니아 아무리 나삐 굴어도 넌 내게 이 순간 다 만화야 순정만화야 주인공은 맨날 맨날 이렇게 밤마다 기도해 Give love 사랑을 좀 주세요 Give love 사랑이 모자라요 매일매일 자라는 사랑을 그녀에게 주는데도 받질 않으니 Give love 사랑을 좀 주세요 Give love 사랑이 모자라요 매일매일 자라는 사랑을 그녀에게 주는데도 받질 않으니 Give love Give love Give love woah yeah 잘못한 것도 없는데 왜 무작정 싫어하고 보는 너 Why cant you understand me 난 너를 좋아한다고 네가 날 싫어해 하는 걸 안 후 부터 샘솟던 의욕이 다 시들고 설레던 내 맘도 끝이겠구나 했는데 또다시 슬금슬금 다가가도 될까 바라보는 것조차 싫어할까 봐 난 몰래 뒤에서 긍긍전전해 점점 해가 지면 달빛 정전에 용기가 나 내 맘을 전부 전해 하지만 그녀와 내 사이 거리 너무 멀어 주고 또 주는 사랑이 길바닥에 다 버려져 낙엽처럼 쌓이네 봄이 되면 흙으로 남아 혹시 기대해 싹이 될까 Give love 사랑을 좀 주세요 Give love 사랑이 모자라요 매일매일 자라는 사랑을 그녀에게 주는데도 받질 않으니 Give love 사랑을 좀 주세요 Give love 사랑이 모자라요 매일매일 자라는 사랑을 그녀에게 주는데도 받질 않으니 Give love Give love Give love Give love Give love Give love woah yeah|
| ... | ... | ... |
