import streamlit as st
import google.generativeai as genai

# 1. Branding & UI
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Powered by AstroMind | Developed by HEMADATH")

# 2. Sidebar for the Key
with st.sidebar:
    st.header("Control Center")
    api_key = st.text_input("Enter your Gemini API Key", type="password")
    st.info("Get a fresh key at: aistudio.google.com")

# 3. The Logic
if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # THE 2026 FIX: Using the current stable 'gemini-2.5-flash'
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Chat Input
        if prompt := st.chat_input("Talk to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Get AI Response
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
    except Exception as e:
        st.error(f"Connection issue: {e}")
else:
    st.warning("👈 Please paste your API key in the sidebar to start!")
