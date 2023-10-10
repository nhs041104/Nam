import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader

from langchain.vectorstores import Chroma

from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")

from google.colab import drive
drive.mount('/content/drive')

fn_dir = "/content/drive/MyDrive/Colab Notebooks/SING/"

loader = PyPDFDirectoryLoader(fn_dir)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

len(documents), len(docs)

db = Chroma.from_documents(docs, embedding=embeddings,
                                 persist_directory=".ver2")
db.persist()

query =""
docs = db.similarity_search(query)

docs[:1]
