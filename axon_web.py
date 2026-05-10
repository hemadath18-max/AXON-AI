import streamlit as st
import google.generativeai as genai

# 1. PAGE SETTINGS
st.set_page_config(page_title="AXON by RC ANAND", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Powered by AstroMind | Developed by RC ANAND")

# 2. THE SIDEBAR
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at: aistudio.google.com")

# 3. INITIALIZE AXON
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Using the corrected model setup
        model = genai.GenerativeModel('gemini-pro')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Ask AXON anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # System instruction for the mentor personality
                full_prompt = f"System: You are AXON, a wise mentor created by RC ANAND. Answer this: {prompt}"
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Waiting for valid key... {e}")
else:
    st.warning("👈 Open the sidebar (click the > arrow at top left) and enter your API key!")
