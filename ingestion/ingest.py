from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

loader = PyPDFLoader("data/PORTARIA Vacina.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(chunks, embeddings)

vectorstore.save_local("vectorstore")

print("Documentos indexados com sucesso")