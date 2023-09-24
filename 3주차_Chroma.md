# 결과
```python
query = "Give Love 부른 가수 누구야?"
docs = db.similarity_search(query)
docs[:5]
```

```python
[Document(page_content='가수 : 악동뮤지션\n\n노래제목 : Give Love', metadata={'source': '/content/drive/MyDrive/Colab Notebooks/SING/AKMU.txt'})
```

