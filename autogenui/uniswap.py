from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
import os

def answer_uniswap_question(question):
    # Загружаем файл
    loader = [PyPDFLoader(os.path.join(os.getcwd(), "docs", "marketer.pdf"))]
    docs = []
    for l in loader:
        docs.extend(l.load())
    # создаём разделитель на чанки
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = text_splitter.split_documents(docs)
    # создаём векторное хранилище изображений
    vector_store = Chroma(
        collection_name="full_documents",
        embeddings_function=OpenAIEmbeddings()
    )
    vector_store.add_documents(docs)
    # диалоговая цепочка
    qa = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0),
        vector_store.as_retriever(),
        memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True),
    )
    response = qa({"question": question})
    return response["answers"]