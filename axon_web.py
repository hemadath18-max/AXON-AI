import streamlit as st
import google.generativeai as genai

# 1. Branding - Your Name is Front and Center!
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. The Professional Connection
try:
    if "GEMINI_API_KEY" in st.secrets:
        # We add transport='rest' to fix the error in your last screenshot
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.warning("Hemadath, please add the API Key to Streamlit Secrets!")
        st.stop()
except Exception as e:
    st.error(f"System connection error: {e}")
    st.stop()

# 3. Chat Interface
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
        response = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with st.chat_message("assistant"):
            st.write(response.text)
    except Exception as e:
        # This handles the error gracefully if Google is busy
        st.error("AXON is processing a lot of data. Try typing your message again!")
