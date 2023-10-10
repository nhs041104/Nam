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

```python
query ="마치 피리부는 사나이 처럼"
```
[Document(page_content='가수:이세계아이돌\n노래제목 :kidding\n노래가사 :졸졸 따라다녀 어떡해 나 마치 피리 부는 사나이처럼 내겐 없어 딴 맘 오늘은 좀 바', metadata={'page': 0, 'source': '/content/drive/MyDrive/Colab Notebooks/SING/이세계아이돌.pdf'})]

---

```python
query ="우산 없이 비가와"
```
[Document(page_content='도 우산 없이 비가 와 홀딱 다 젖어도 좋아 I love it because I love you 우리 관계 디비디', metadata={'page': 0, 'source': '/content/drive/MyDrive/Colab Notebooks/SING/악뮤.pdf'})]

---

```python
query ="밤은 다시 길고 깊어졌네"
```
[Document(page_content='가수:십센치\n노래제목 :그라데이션\n노래가사 :밤은 다시 길고 깊어졌네 나는 점점 너로 잠 못 들게 돼 글로 적어내긴 어려운 이 \n기분을 너도 느꼈으면 좋겠는데 너는 아무 생각 없이 몇 번 나를 지나가며 웃은 거라지만 나\n의 하얀 옷에 너의 잉크가 묻어 닦아낼 수 없을 만큼 번졌네 달콤한 색감이 물들어 조금씩 정\n신을 차렸을 땐 알아볼 수도 없지 가득 찬 마음이 여물다 못해 터지고 있어 내일은 말을 걸어\n봐야지 요즘 노랜 뭔가 맘에 안 들어 네게 불러 주기엔 좀 어려워서 나름 며칠 밤을 새워 연\n습했지만 네게 들려주기엔 무리인 것 같아 너는 번질수록 진해져 가고 나의 밤은 좀 더 길고 \n외롭지만 하루 종일 떠오르는 너의 얼굴은 방을 가득 채워 무지개같이 달콤한 색감이 물들어 \n조금씩 정신을 차렸을 땐 알아볼 수도 없지 가득 찬 마음이 여물다 못해 터지고 있어 내일은 \n말을 걸어봐야지 바람을 맞고 빗물에 젖어 나의 색감도 흐려지겠지만 너는 항상 빛에 반짝일', metadata={'page': 0, 'source': '/content/drive/MyDrive/Colab Notebooks/SING/10센치.pdf'})]

---

```python
query ="Money  makes  me  feel  better"
```
[Document(page_content="가수:지올팍\n노래제목 :Christian\n노래가사 :Money makes me feel better You told me it was a ticket to hell, how \ncome? Do you think that I'm a devil? Sex makes me feel better How could you \njudge me? I know you don't deserve to Now you act like a Pharisee When I was \npoor, my mom was stressed out Now look, money made me a good boy to my \nmom When I was poor, I was like a hungry fox Now look, I saved a lotta buddies \nfrom the basement I just bought a Christian, it's blinging on my body I'm toasting", metadata={'page': 0, 'source': '/content/drive/MyDrive/Colab Notebooks/SING/지올팍.pdf'})]
