import streamlit as st

# 1. Your Brand (This stays forever!)
st.set_page_config(page_title="AXON AI", page_icon="🚀")
st.title("✨ AXON: The Maverick Mentor")
st.caption("Developed by Hemadath | Powered by AstroMind")

st.success("✅ System Online! Hemadath, your app is officially live.")

# 2. Local "Brain" (No API key needed!)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hemadath, I am AXON. You built me. Today was a hard battle, but you won because your website is LIVE!"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Talk to your creation..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # AXON replies locally for now
    response = "Buddy, I hear you! My API connection is just waiting for Google to wake up, but look—I'm running on YOUR website!"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
