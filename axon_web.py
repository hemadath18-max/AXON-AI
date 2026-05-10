import streamlit as st
import google.generativeai as genai

# 1. Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Stronger Connection Logic
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # This 'latest' tag helps Google find the fastest server for you
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("Hemadath, the Secret Key is missing!")
    st.stop()

# 3. Chat System
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Talk to AXON..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        # We add a small 'safety' check here
        response = model.generate_content(prompt)
        if response:
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.write(response.text)
    except Exception as e:
        st.info("I'm waking up... try sending that one more time, Hemadath!")
