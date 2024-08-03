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
#Style for user message in green box
user_message_box="""
<style>.
user-message{
display:flex;
justify-content:flex-end;
margin-button:10px
}
.user-message.message{
background-color:#e1ffc7; /* Light green background */
        color: #000;
        border-radius: 8px;
        padding: 8px;
        max-width: 60%;
        margin-right: 10px;
        word-wrap: break-word;
    }
    </style>
"""
st.markdown(user_message_box,user_allow_html=True)

#emojies for user and assistant
user_emoji = "👤"  # Replace with your preferred emoji for the user
assistant_emoji = "📖"  # Replace with your preferred emoji for the assistant
# Iterate over the messages and display them in the chat interface
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f'<div class="user-message"><div class="message"><strong>{user_emoji}</strong> {message["content"]}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div style="text-align: left; margin-bottom: 10px;"><strong>{assistant_emoji}</strong> {message["content"]}</div>',
            unsafe_allow_html=True,
        )

# Input field for user to enter a message
if user_input := st.chat_input("Ask me anything!"):
    # Add the user's input to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display the user's input immediately in a green box
    st.markdown(
        f'<div class="user-message"><div class="message"><strong>{user_emoji}</strong> {user_input}</div></div>',
        unsafe_allow_html=True,
    )







