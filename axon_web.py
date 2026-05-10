import streamlit as st
import google.generativeai as genai

# Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by RC ANAND")

# Sidebar
with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Paste Gemini API Key", type="password")

if api_key:
    try:
        # THE MAGIC FIX: This line tells Google to use the stable version
        genai.configure(api_key=api_key)
        
        # We use 'gemini-1.5-flash' which is the most reliable
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Talk to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generating response
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
    except Exception as e:
        # If there's an error, it will show a friendly message
        st.error("Almost there! Please check if your API Key is correct and has Gemini 1.5 Flash enabled.")
else:
    st.info("👈 Open the sidebar (click the small > arrow) and paste your API key!")
