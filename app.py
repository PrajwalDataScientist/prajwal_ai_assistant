import streamlit as st
from agents.router import ask_agent
import json

# Load profile
def load_profile():
    with open('config/profile.json', 'r', encoding='utf-8') as file:
        profile_data = json.load(file)
    return profile_data

profile = load_profile()

# Page config
st.set_page_config(page_title="Prajwal's AI Assistant", page_icon="🤖", layout="wide")

# Sidebar
with st.sidebar:
    st.image("agents/profile_id.jpg", width=200)  # Your profile image
    st.title("Prajwal B")
    st.markdown(f"📧 **Email:** [ {profile['email']} ](https://mail.google.com/mail/?view=cm&fs=1&to={profile['email']}&su=Discussion%20Request&body=Hey%20Prajwal%2C%20I%20would%20like%20to%20discuss%20with%20you.%20Please%20let%20me%20know%20your%20available%20time.)")
    st.markdown(f"🔗 [LinkedIn]({profile['linkedin']})")
    st.markdown(f"🐙 [GitHub]({profile['github']})")
    st.markdown(f"🐳 [DockerHub]({profile['dockerhub']})")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()



# Header (Fixed visually)
st.markdown("""
    <div style='position: sticky; top: 0; background-color: #f0f2f6; padding: 15px; border-radius: 10px; z-index: 999; text-align: center;'>
        <h1>🤖 Prajwal's Personal AI Assistant</h1>
        <h4>Ask me anything about Prajwal 🚀</h4>
    </div>
""", unsafe_allow_html=True)

# Chat history state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat history display
chat_container = st.container()

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        chat_container.markdown(f"""
        <div style='text-align: right; background-color: #dcf8c6; padding: 10px; border-radius: 10px; margin: 5px 0;'>
            <strong>You:</strong> {chat['content']}
        </div>
        """, unsafe_allow_html=True)
    else:
        chat_container.markdown(f"""
        <div style='text-align: left; background-color: #f1f0f0; padding: 10px; border-radius: 10px; margin: 5px 0;'>
            <strong>Assistant:</strong> {chat['content']}
        </div>
        """, unsafe_allow_html=True)

# Fixed input at the bottom
user_input = st.chat_input("Type your message here...")

if user_input:
    # Save user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get assistant response
    response = ask_agent(user_input)

    # Save assistant response
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Rerun to scroll to bottom
    st.rerun()
