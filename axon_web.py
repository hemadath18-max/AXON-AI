import streamlit as st
import google.generativeai as genai

# 1. Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Sidebar for the Key
with st.sidebar:
    st.header("Settings")
    user_key = st.text_input("Paste API Key:", type="password")

# 3. Chat Logic
if user_key:
    try:
        # Simple connection
        genai.configure(api_key=user_key)
        
        # WE USE 'gemini-1.5-flash' - the most stable name!
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Say something to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # Get the response
            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.write(response.text)
                
    except Exception as e:
        st.error("Wait a moment, then try again!")
else:
    st.warning("Hemadath, paste your key in the sidebar to start!")
