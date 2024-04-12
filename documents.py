import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Epsilla
from pyepsilla import vectordb
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

st.title("Chat with Documents")

load_dotenv()
embeddings = OpenAIEmbeddings()
# Connect to Epsilla as knowledge base.
client = vectordb.Client()
vector_store = Epsilla(
  client,
  embeddings,
  db_path="/tmp/localchatdb",
  db_name="LocalChatDB"
)
vector_store.use_collection("LocalChatCollection")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, 
                                chain_type="stuff",
                                retriever=vector_store.as_retriever(),
                                return_source_documents=True,
                                verbose=True
                                )


#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#React to user input
if prompt := st.chat_input("Whats up?"):
    #Display user message in chat message container
    with st.chat_message(name="user"):
        st.markdown(prompt)
    
    #Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Echo: {prompt}"
    response = qa({"query": prompt})
    print('Source', response['source_documents'][0])

    #Display assistant response in chat message container
    with st.chat_message(name="Assistant"):
        st.markdown(response['result'])

    #Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response['result']})