# 3주차 노래 가사 텍스트 파일 색인&검색
## 목표
- 파일에 있는 노래 가사 불용어 제거
- 파일에 원하는 단어 검색
- 해당 단어가 들어간 파일 불러오기

```python
import os
import re
```
os 모듈과 re 모듈을 가져온다. os 모듈은 운영 체제와 상호 작용하는 데 사용되고 re 모듈은 정규 표현식을 사용하여 문자열을 처리하는 데 사용된다.

```python
data_folder = "/content/drive/MyDrive/Colab Notebooks/SING"
```
검색 대상이 될 폴더 경로를 변수 data_folder에 저장한다. 이 코드에서는 Google Colab 환경에서 /content/drive/MyDrive/Colab Notebooks/SING 경로를 사용했다.

```python
search_word = input("검색할 단어를 입력하세요: ")
```
검색할 단어를 입력한다.

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
                print("파일 이름:", file)
                print("본문 내용:", cleaned_content)
                print("=" * 80)
```
사용자가 입력한 검색어 search_word가 cleaned_content에 포함되어 있는지 확인하고, 검색어가 파일 내에 발견된 경우 해당 파일의 이름과 파일의 내용을 출력한다. 마지막으로 각 파일을 구분하기 위해 =을 80번 출력해서 가독성을 높혔다.
