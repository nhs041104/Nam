import os
import re

data_folder = "/content/drive/MyDrive/Colab Notebooks/SING"

search_word = input("검색할 단어를 입력하세요: ")

for root, dirs, files in os.walk(data_folder):
    for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()

            cleaned_content = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣\sA-Za-z]", "", file_content)

            if search_word in cleaned_content:
                print("파일 이름:", file)
                print("본문 내용:", cleaned_content)
                print("\n=\n" * 80)
