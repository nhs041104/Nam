import os
import re
import pandas as pd

data_folder = "/content/drive/MyDrive/Colab Notebooks/SING"

search_word = input("검색할 단어를 입력하세요: ")

file_info_list = []

for root, dirs, files in os.walk(data_folder):
    for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()

            cleaned_content = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣\sA-Za-z]", "", file_content)

            if search_word in cleaned_content:
                file_info_list.append({"파일 이름": file, "가사": cleaned_content})
               
df = pd.DataFrame(file_info_list)
df
