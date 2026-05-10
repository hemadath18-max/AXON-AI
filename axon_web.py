import streamlit as st
import google.generativeai as genai

# 1. Page Header
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Connection Logic
try:
    if "GEMINI_API_KEY" in st.secrets:
        # We use transport='rest' for mobile stability
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')
        # Switching to 'gemini-pro' - the most stable model ever made
        model = genai.GenerativeModel('gemini-pro')
    else:
        st.error("Hemadath, the Key is missing in Secrets!")
        st.stop()
except Exception as e:
    st.error(f"Setup Error: {e}")
    st.stop()

# 3. Chat Logic
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
        # Get response
        response = model.generate_content(prompt)
        
        # Check if response actually has text
        if response and response.text:
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.write(response.text)
        else:
            st.info("I'm connected, but I couldn't find the answer. Try asking again!")
    except Exception as e:
        st.error("AXON is stretching! Give him one more message.")
