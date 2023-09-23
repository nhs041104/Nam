import os: os 모듈을 가져옵니다. os 모듈은 운영 체제와 상호 작용하는 데 사용됩니다.

import re: re 모듈을 가져옵니다. re 모듈은 정규 표현식을 사용하여 문자열을 처리하는 데 사용됩니다.

data_folder = "/content/drive/MyDrive/Colab Notebooks/SING": 검색 대상이 될 폴더 경로를 변수 data_folder에 저장합니다. 이 코드에서는 Google Colab 환경에서 /content/drive/MyDrive/Colab Notebooks/SING 경로를 사용하고 있습니다.

search_word = input("검색할 단어를 입력하세요: "): 사용자로부터 검색할 단어를 입력받습니다. input() 함수를 사용하여 사용자에게 메시지를 표시하고, 사용자의 입력을 search_word 변수에 저장합니다.

for root, dirs, files in os.walk(data_folder):: os.walk() 함수를 사용하여 data_folder 경로 아래의 모든 파일과 디렉토리를 순회하는 루프를 시작합니다. root는 현재 디렉토리의 경로를 나타내고, dirs는 현재 디렉토리 내의 하위 디렉토리를 나타냅니다. files는 현재 디렉토리 내의 파일 목록을 나타냅니다.

for file in files:: 현재 디렉토리 내의 각 파일에 대한 루프를 시작합니다.

file_path = os.path.join(root, file): 현재 파일의 경로를 file_path 변수에 저장합니다. os.path.join() 함수는 디렉토리 경로와 파일 이름을 결합하여 완전한 파일 경로를 생성합니다.

with open(file_path, "r", encoding="utf-8") as f:: 파일을 읽기 모드("r")로 엽니다. encoding="utf-8"은 파일을 UTF-8 인코딩으로 열도록 지정합니다. 이것은 한글 및 다른 유니코드 문자를 올바르게 처리하기 위한 것입니다.

file_content = f.read(): 파일 내용을 읽어와 file_content 변수에 저장합니다.

cleaned_content = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣\sA-Za-z]", "", file_content): 정규 표현식을 사용하여 파일 내용에서 한글, 공백, 영어 (A-Z 및 a-z)를 제외한 모든 문자를 제거하고, 결과를 cleaned_content 변수에 저장합니다. 이렇게 함으로써 파일 내용에서 원하는 문자만 남게 됩니다.

if search_word in cleaned_content:: 사용자가 입력한 검색어 search_word가 cleaned_content에 포함되어 있는지 확인합니다.

print("파일 이름:", file): 검색어가 파일 내에 발견된 경우 해당 파일의 이름을 출력합니다.

print("본문 내용:", cleaned_content): 검색어가 발견된 파일의 내용을 출력합니다.

print("\n=\n" * 80): 각 파일 결과 사이에 구분선을 출력합니다. 이 구분선은 80번 반복되며 개행 문자로 인해 결과가 잘 구분되도록 합니다.
