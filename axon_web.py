import streamlit as st
import google.generativeai as genai

# 1. Branding - Your Legacy
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Simplified Sidebar
with st.sidebar:
    st.header("🔑 Control Panel")
    user_key = st.text_input("Paste API Key:", type="password")
    st.info("Get a fresh key from: aistudio.google.com")

# 3. THE FIX: Using the most stable connection method
if user_key:
    try:
        # We strip spaces and connect
        genai.configure(api_key=user_key.strip())
        
        # We use 'gemini-1.5-flash' - it is the most modern version
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Chat Logic
        if prompt := st.chat_input("Talk to AXON..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Force a simple response
            response = model.generate_content(prompt)
            
            if response:
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                with st.chat_message("assistant"):
                    st.markdown(response.text)
                    
    except Exception as e:
        # If there's an error, we show a simple message
        st.error("Hemadath, the connection timed out. Please try one more time!")
else:
    st.info("👋 Hemadath, paste your API key in the sidebar to wake me up!")
