import streamlit as st
import google.generativeai as genai

# =========================
# 1. UI CONFIG
# =========================
st.set_page_config(page_title="AXON AI", page_icon="🚀", layout="centered")

st.title("✨ AXON: The Maverick Mentor")
st.caption("Powered by AstroMindAI | Built by HEMADATH")

# =========================
# 2. SIDEBAR API KEY
# =========================
with st.sidebar:
    st.header("Control Center")
    api_key = st.text_input("Enter your Gemini API Key", type="password")
    st.info("Get your key from Google AI Studio")

# =========================
# 3. CHECK API KEY
# =========================
if not api_key:
    st.warning("👈 Please enter your API key to start AXON AI")
    st.stop()

# =========================
# 4. CONFIGURE MODEL
# =========================
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro")
except Exception as e:
    st.error(f"Model setup failed: {e}")
    st.stop()

# =========================
# 5. SESSION MEMORY
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# 6. CHAT INPUT
# =========================
prompt = st.chat_input("Talk to AXON...")

if prompt:
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response (safe handling)
    try:
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error from AI: {e}"

    # Assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
