import streamlit as st
import google.generativeai as genai

# 1. Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Simple Sidebar for your Key
with st.sidebar:
    st.header("Settings")
    user_key = st.text_input("Paste your Gemini API Key here:", type="password")
    st.info("Get your key from: aistudio.google.com")

# 3. Connection Logic
if user_key:
    try:
        genai.configure(api_key=user_key, transport='rest')
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Chat System
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Talk to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.write(response.text)
                
    except Exception as e:
        st.error(f"Try pasting the key again, Hemadath! Error: {e}")
else:
    st.warning("Please paste your API key in the sidebar to start chatting!")
