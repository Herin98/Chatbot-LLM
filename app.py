import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os


load_dotenv() 
llm=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.5,google_api_key=os.getenv("GOOGLE_API_KEY"),convert_system_message_to_human=True)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

def get_chat_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=llm.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain-Gemini Application")

input=st.text_input("Input: ",key="input")
response=get_chat_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is ")
    st.write(response)
