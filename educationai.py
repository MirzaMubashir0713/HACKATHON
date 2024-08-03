import requests
import streamlit as st 
# Write your api end point and key
API_URL="https://api.groq.com/openai/v1/chat/completions"
API_KEY="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" 
#replace with your official key and url
headers={
    "Authorization":f"Bearer{API_KEY}",
}
#fucntion to send message to the llama 3 api and receive response
def call_llama_api(messages):
    payload={    
        "model":"llama3-8b-8192",
        "messages":messages
    }
response=requests.post(API_URL,headers=headers)
response.status_for_status()
#rasie an exception for http errors
#slidbar with a button to clear the chat history with st.sidebar:
if st.button("clear Chat History"):
    st.session_state["messages"]=[]
#show the title 
st.title("<EDUCATION AI>")





