import streamlit as st
import google.generativeai as genai

# 1. Your Pride & Joy
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. The Key Entry
with st.sidebar:
    st.header("🔑 Control Panel")
    user_key = st.text_input("Paste API Key here:", type="password")
    st.markdown("---")
    st.write("Keep going, Hemadath!")

# 3. The Stable Brain
if user_key:
    try:
        genai.configure(api_key=user_key)
        # We use gemini-pro because it's the most reliable!
        model = genai.GenerativeModel('gemini-pro')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Talk to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # Direct call
            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.write(response.text)
                
    except Exception as e:
        st.error("Just a small glitch. Try hitting Enter again!")
else:
    st.info("👋 Welcome! Hemadath, please paste your key in the sidebar to begin.")
