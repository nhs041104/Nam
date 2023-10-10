# 수정 사항

```python
# 수정된 코드
from langchain.text_splitter import RecursiveCharacterTextSplitter
```

---

```python
# 수정된 코드
embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")
```

---

```python
# 수정된 코드
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
```

# 결과
```python
query ="나는 읽기 쉬운 마음이야"
```
[Document(page_content='가수:잔나비\n노래제목 :주저하는 연인들을 위해\n노래가사 :나는 읽기 쉬운 마음이야 당신도 쓱 훑고 가셔요 달랠 길 없는 외로운 마음 있지 머\n물다 가셔요 내게 긴 여운을 남겨줘요 사랑을 , 사랑을 해줘요 할 수 있다면 그럴 수만 있다면 \n새하얀 빛으로 그댈 비춰 줄게요 그러다 밤이 찾아오면 우리 둘만의 비밀을 새겨요 추억할 그 \n밤 위에 갈피를 꽂고선 남몰래 펼쳐보아요 나의 자라나는 마음을 못 본채 꺾어 버릴 순 없네 \n미련 남길 바엔 그리워 아픈 게 나아 서둘러 안겨본 그 품은 따스할 테니 그러다 밤이 찾아오\n면 우리 둘만의 비밀을 새겨요 추억할 그 밤 위에 갈피를 꽂고선 남몰래 펼쳐보아요 언젠가 \n또 그날이 온대도 우린 서둘러 뒤돌지 말아요 마주 보던 그대로 뒷걸음치면서 서로의 안녕을 \n보아요 피고 지는 마음을 알아요 다시 돌아온 계절도 난 한동안 새 활짝 피었다 질래 또 한 \n번 영원히 그럼에도 내 사랑은 또 같은 꿈을 꾸고 (라 라라라 라랄라 랄라라라 ) 그럼에도 꾸', metadata={'page': 0, 'source': '/content/drive/MyDrive/Colab Notebooks/SING/잔나비.pdf'})]

---
