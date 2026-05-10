import streamlit as st
import google.generativeai as genai

# 1. Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Powered by AstroMind | Developed by RC ANAND")

# 2. Sidebar Setup
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at: aistudio.google.com")

# 3. Main Chat Logic
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Using the absolute latest stable model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Ask AXON anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Waiting for valid key... {e}")
else:
    st.info("👈 Please enter your API Key in the sidebar to begin.")
