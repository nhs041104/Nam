# 결과
```python
query = "Give Love 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:1]
```

[Document(page_content='가수 : 악동뮤지션\n\n노래제목 : Give Love', metadata={'source': '/content/drive/MyDrive/Colab Notebooks/SING/AKMU.txt'})]

---

```python
query = "겨울봄 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:1]
```
[Document(page_content='가수 : 이세계 아이돌\n\n노래제목 : 겨울봄', metadata={'source': '/content/drive/MyDrive/Colab Notebooks/SING/이세돌.txt'})]

---

```python
query = "짝사랑 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:1]
```
[Document(page_content='가수 : 십센치\n\n노래제목 : 짝사랑', metadata={'source': '/content/drive/MyDrive/Colab Notebooks/SING/십센치.txt'})]

---

```python
query = "사랑하긴 했었나요 스쳐가는 인연이였나요 어쩌구 저쩌구 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:1]
```
[Document(page_content='가수 : 잔나비\n\n노래제목 : 사랑하긴 했었나요 스쳐가는 인연이었나요 짧지 않은 우리 함께했던 시간들이 자꾸 내 마음을 가둬두네\n\n노래가사 : 사랑하긴 했었나요\n\n스쳐가는 인연이었나요', metadata={'source': '/content/drive/MyDrive/Colab Notebooks/SING/Jannabi.txt'})]

---

```python
query = "Christain 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:1]
```
[Document(page_content='가수 : 지올팍\n\n지올팍 노래제목 : Christian', metadata={'source': '/content/drive/MyDrive/Colab Notebooks/SING/Christian.txt'})]

---

```python
query = "Christain 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:1]
```

