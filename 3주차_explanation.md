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
    file_info_list.append({"파일 이름": file, "가사": cleaned_content})
```
이 부분은 검색어인 search_word가 파일 내용(cleaned_content)에 포함되어 있는지 확인하고, 포함되어 있다면 파일 정보를 file_info_list라는 리스트에 추가하는 역할을 한다.

```python
df = pd.DataFrame(file_info_list)
df
```
마지막으로 pandas를 이용해 결과물을 출력한다.


# 출력 결과
## 검색 단어 "사랑"

|    | 파일 이름 | 가사 |
|-------|--------|---------|
| 0 | AKMU.txt | Why baby 뭐가문제야 baby Woah Woah Woah woah Hey woah Woah Anyone please Woah Woah woah 제발 사랑 좀 줘요..... |
| 1 | Jannabi.txt | 사랑하긴 했었나요 스쳐가는 인연이었나요 짧지 않은 우리 함께했던 시간들이 자꾸 내 마음을 가둬두네..... |
| 2 | 10CM.txt |그대의 표정이 너무 차가와서 나의 말은 닿기도 전에 얼어붙네 그대의 말투가 너무 건조해서 나의 맘은 열기도 전에 시들었지 혼자 나누는 사랑도 아름답지만..... |

## 검색 단어 "You"

|    | 파일 이름 | 가사 |
|-------|--------|---------|
| 0 | Christian.txt | Money makes me feel better You told me it was a ticket to hell how come Do you think that .....|
| 1 | AKMU.txt | Why baby 뭐가문제야 baby Woah Woah Woah woah Hey woah Woah Anyone please Woah Woah woah 제발 사랑 좀 줘요 네가 날 싫어해 하는 걸 알아 나는 서운해 그런 날 왜 너는 못 이해해 You dont understand 난 너를 좋아한다고..... |
| 2 | Jannabi.txt |사랑하긴 했었나요 스쳐가는 인연이었나요 짧지 않은 우리 함께했던 시간들이 자꾸 내 마음을 가둬두네 yeah 누가 내 가슴에다 불을 질렀나 누가 내 심장에다 못을 박았나 그대의 눈빛은 날 얼어붙게 해 그대여 다시 내게 마음을 주오 Ooh ooh baby I need you..... |


## 검색 단어 ""

|    | 파일 이름 | 가사 |
|-------|--------|---------|
| 0 | AKMU.txt | Why baby 뭐가문제야 baby Woah Woah Woah woah Hey woah Woah Anyone please Woah Woah woah 제발 사랑 좀 줘요 네가 날 싫어해 하는 걸 알아 나는 서운해 .....|
| 1 | Jannabi.txt | 사랑하긴 했었나요 스쳐가는 인연이었나요 짧지 않은 우리 함께했던 시간들이 자꾸 내 마음을 가둬두네 yeah 누가 내 가슴에다 불을 질렀나 누가 내 심장에다 못을 박았나 그대의 눈빛은 날 얼어붙게 해 ..... |
| 2 | Isegye.txt |처음이란건 돌아보면 네가 흘렸던 작은 말들 무심한듯 담았어 나도 모르게 하늘을 봐도 알수없어 네가 말하던 그 계절이 오면 혹시라도 그대가 여기 흰 눈 속에서 보이는 시린기억이 스쳐요 그댈 본다면 나을까요 날 붙잡던 손 날 보던 그 두 눈이..... |
