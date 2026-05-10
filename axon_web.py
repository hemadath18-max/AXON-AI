import streamlit as st
import google.generativeai as genai

# 1. Your Brand
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Sidebar
with st.sidebar:
    st.header("🔑 Control Panel")
    user_key = st.text_input("Paste API Key:", type="password")

# 3. The Brain
if user_key:
    try:
        genai.configure(api_key=user_key)
        # We use the most basic model name that Google ALWAYS recognizes
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

            # This is the line that gets the answer!
            response = model.generate_content(prompt)
            
            if response.text:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                with st.chat_message("assistant"):
                    st.write(response.text)
            else:
                st.write("AXON is thinking... try one more time!")
                
    except Exception as e:
        st.error(f"Almost there! Just re-paste your key. Error: {e}")
else:
    st.info("👋 Hemadath, paste your key in the sidebar to start!")
