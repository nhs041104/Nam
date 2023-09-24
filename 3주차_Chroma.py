import os
import pandas as pd

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

from langchain.embeddings import LlamaCppEmbeddings, HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()

from google.colab import drive
drive.mount('/content/drive')

fn_dir = "/content/drive/MyDrive/Colab Notebooks/SING"

loader = DirectoryLoader(fn_dir)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

len(documents), len(docs)

db = Chroma.from_documents(docs, embedding=embeddings,
                                 persist_directory="lyrics_index_hf")
db.persist()

query = "질문을 입력하세"
docs = db.similarity_search(query)

docs[:1]
