from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from glob import glob
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()
files = glob("./cvs/*")

embeddings = OpenAIEmbeddings()

print('Files: ')
for file in files:
    print(file)
    if file.endswith('.pdf'):
        loader = PyPDFLoader(file)
    else:
        loader = TextLoader(file)
    documents = loader.load()
    splitted_documents = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200).split_documents(documents)


    Chroma.from_documents(
        splitted_documents, 
        embeddings, 
        persist_directory="./chroma_db")