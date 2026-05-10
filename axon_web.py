import streamlit as st
import google.generativeai as genai

# =========================
# 1. PAGE SETUP
# =========================
st.set_page_config(page_title="AXON AI", page_icon="🚀", layout="centered")

st.title("✨ AXON AI: Maverick Mentor")
st.caption("Powered by Gemini AI | Built by AstroMindAI")

# =========================
# 2. API KEY INPUT
# =========================
with st.sidebar:
    st.header("🔐 Control Panel")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get key from: https://aistudio.google.com/")

# Stop if no key
if not api_key:
    st.warning("👈 Please enter your API key to continue")
    st.stop()

# =========================
# 3. CONFIGURE GEMINI
# =========================
try:
    genai.configure(api_key=api_key)

    # MOST STABLE MODEL (IMPORTANT FIX)
    model = genai.GenerativeModel("models/gemini-1.5-flash")

except Exception as e:
    st.error(f"Setup Error: {e}")
    st.stop()

# =========================
# 4. CHAT MEMORY
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# 5. USER INPUT
# =========================
prompt = st.chat_input("Talk to AXON AI...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response (SAFE)
    try:
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
