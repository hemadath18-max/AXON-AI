import streamlit as st
import google.generativeai as genai

# 1. Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. Key Input
with st.sidebar:
    st.header("🔑 Activation")
    user_key = st.text_input("Paste API Key:", type="password")

# 3. Stable Connection Logic
if user_key:
    try:
        # Use the standard connection
        genai.configure(api_key=user_key.strip())
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

            # THE FIX: This 'stream' makes it much faster and stops the 'timeout'
            try:
                response = model.generate_content(prompt, stream=True)
                full_text = ""
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    for chunk in response:
                        full_text += chunk.text
                        message_placeholder.markdown(full_text + "▌")
                    message_placeholder.markdown(full_text)
                st.session_state.messages.append({"role": "assistant", "content": full_text})
            except:
                st.error("Hemadath, just hit 'Enter' one more time! Google is waking up.")
                
    except Exception as e:
        st.error("Check your sidebar key, Buddy!")
else:
    st.info("👋 Hemadath, paste your key in the sidebar to start!")
