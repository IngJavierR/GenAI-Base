import os
import streamlit as st
from langchain import OpenAI, SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv

st.title("SQL Bot")

load_dotenv()

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{os.environ.get('DBUSER')}:{os.environ.get('DBPASS')}@localhost:5432/{os.environ.get('DATABASE')}",
)

# setup llm
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=False)

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
    response = db_chain.run(prompt)

    #Display assistant response in chat message container
    with st.chat_message(name="Assistant"):
        st.markdown(response)

    #Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})