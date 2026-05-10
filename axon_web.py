import streamlit as st
import google.generativeai as genai

# 1. Branding - Your Identity
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. The Sidebar Key (The simplest way)
with st.sidebar:
    st.header("🔑 Activation")
    user_key = st.text_input("Paste API Key:", type="password")
    st.info("Get a fresh key from: aistudio.google.com")

# 3. The "Smart" Connection Logic
if user_key:
    try:
        # We clean the key automatically
        genai.configure(api_key=user_key.strip())
        
        # We use the most updated model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Chat Input
        if prompt := st.chat_input("Ask Hemadath's AI anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # GETTING THE RESPONSE
            with st.spinner("AXON is thinking..."):
                try:
                    response = model.generate_content(prompt)
                    if response.text:
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                        with st.chat_message("assistant"):
                            st.markdown(response.text)
                    else:
                        st.error("Google didn't send text. Try asking again!")
                except Exception as api_error:
                    st.error(f"Connection error. Please re-paste your key! {api_error}")

    except Exception as e:
        st.error(f"Setup error: {e}")
else:
    st.warning("👋 Hemadath, your app is ready! Just paste your API Key in the sidebar to start.")
