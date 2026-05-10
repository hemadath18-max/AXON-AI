import streamlit as st
import google.generativeai as genai

# 1. WEBSITE SETTINGS
st.set_page_config(page_title="AXON by RC ANAND", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Powered by AstroMind | Developed by RC ANAND")

# 2. THE SECRET KEY (Safety First!)
# On a website, we let the user put their own key for privacy
with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key", type="password")
    "[Get a Google API key](https://aistudio.google.com/app/apikey)"

# 3. INITIALIZE AXON
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask AXON anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Please add your API key in the sidebar to wake AXON.")
