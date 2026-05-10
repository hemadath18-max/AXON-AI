import streamlit as st
import google.generativeai as genai

# Branding
st.set_page_config(page_title="AXON AI")
st.title("✨ AXON: The Maverick Mentor")
st.write("Developed by RC ANAND")

# Sidebar for Key
with st.sidebar:
    api_key = st.text_input("Paste Gemini API Key here:", type="password")

if api_key:
    try:
        # THE FIX: We use a very simple setup here
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Chat interface
        user_input = st.chat_input("Talk to AXON...")
        
        if user_input:
            # Show your message
            st.session_state.chat_history.append(("user", user_input))
            
            # Get AXON's answer
            response = model.generate_content(user_input)
            st.session_state.chat_history.append(("axon", response.text))

        # Display the conversation
        for role, text in st.session_state.chat_history:
            with st.chat_message(role):
                st.write(text)

    except Exception as e:
        st.error(f"Check your API Key! Error: {e}")
else:
    st.warning("👈 Please paste your API Key in the sidebar to wake up AXON!")
