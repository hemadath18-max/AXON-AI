import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AXON AI")
st.title("✨ AXON: The Maverick Mentor")
st.write("Developed by RC ANAND")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Gemini API Key", type="password")

if api_key:
    try:
        # THE FIX: This forces the stable API version
        genai.configure(api_key=api_key, transport='rest')
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

            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👈 Open the sidebar (arrow at top left) and paste your API key!")
