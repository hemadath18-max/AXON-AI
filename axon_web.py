import streamlit as st
import google.generativeai as genai

# 1. Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Control Panel
with st.sidebar:
    st.header("🔑 Settings")
    user_key = st.text_input("Paste API Key:", type="password")

# 3. The Stable Brain
if user_key:
    try:
        # THE FIX: This connects to Google correctly
        genai.configure(api_key=user_key)
        
        # Using the exact name Google wants right now
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Talk to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # Get the response
            response = model.generate_content(prompt)
            
            if response.text:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                with st.chat_message("assistant"):
                    st.write(response.text)
                    
    except Exception as e:
        # This will tell us if it's just a typo in the key
        st.error("Check your key and try one more time!")
else:
    st.info("👋 Hemadath, paste your key in the sidebar to begin!")
