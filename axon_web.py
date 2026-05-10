import streamlit as st
import google.generativeai as genai

# 1. Page Branding
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by RC ANAND | Powered by AstroMind")

# 2. THE SECRET CONNECTION
# This part looks into the 'Secrets' vault you just filled
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Wait! The Secret Key is missing from Streamlit Settings.")
        st.stop()
except Exception as e:
    st.error(f"Connecting to brain... {e}")
    st.stop()

# 3. Simple Chat Interface (No Sidebar!)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Take new input
if prompt := st.chat_input("Talk to AXON..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Get AXON's reply automatically
    response = model.generate_content(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)
