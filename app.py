import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="✨Gemini AI Bot✨", page_icon="🤖")


st.markdown("""
    <style>
        .user_message { background-color: #536493 ; color: white; padding: 10px; border-radius: 8px; margin-bottom: 10px; }
        .ai_message { background-color: #9B7EBD; color: white; padding: 10px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("✨Gemini AI Bot✨")

f = open("api_key.txt")
key = f.read()

genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="You are an AI Data Science Tutor. Only resolve data science doubts.")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.markdown('<div class="ai_message">Hi❕, How may I help you?</div>', unsafe_allow_html=True)

chat = model.start_chat(history=st.session_state['chat_history'])

# Display previous chat messages
for msg in chat.history:
    role_class = "user_message" if msg.role == "user" else "ai_message"
    st.markdown(f'<div class="{role_class}">{msg.parts[0].text}</div>', unsafe_allow_html=True)

# Chat input
user_prompt = st.chat_input()

if user_prompt:
    st.markdown(f'<div class="user_message">{user_prompt}</div>', unsafe_allow_html=True)
    response = chat.send_message(user_prompt)
    st.markdown(f'<div class="ai_message">{response.text}</div>', unsafe_allow_html=True)
    st.session_state['chat_history'] = chat.history
