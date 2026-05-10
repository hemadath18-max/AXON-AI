import streamlit as st
import google.generativeai as genai

# 1. Page Header
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

# 2. THE MASTER CONNECTION
try:
    if "GEMINI_API_KEY" in st.secrets:
        # Connect to Google with a clean rest transport
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')
        
        # We tell Google: "Don't block anything, this is a safe student project"
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            safety_settings=safety_settings
        )
    else:
        st.error("Hemadath, please put the API Key in the Streamlit Secrets box!")
        st.stop()
except Exception as e:
    st.error(f"Setup Error: {e}")
    st.stop()

# 3. Chat System
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Talk to AXON..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # THE BRAIN PUSH
    try:
        # We use a very simple call to get the text directly
        response = model.generate_content(prompt)
        
        if response.text:
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.write(response.text)
        else:
            st.warning("Google sent an empty reply. Try a different question!")
            
    except Exception as e:
        # If there is a real error, we want to see EXACTLY what it is
        st.error(f"Error: {str(e)}")
