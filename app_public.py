import streamlit as st
import datetime
import urllib.request
import urllib.parse

CREATOR_NAME = "Abiodun Ayomide"
LIVE_DATE_OBJECT = datetime.datetime.now()
FULL_DATE_STRING = LIVE_DATE_OBJECT.strftime("%B %d, %Y")

st.set_page_config(page_title="AthenAI Global", page_icon="🦉", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #F8FAFC; }
    .main-title {
        font-size: 3rem !important; font-weight: 700; color: #38BDF8;
        text-align: center; margin-bottom: 1rem;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }
    .chat-bubble-user {
        background-color: #1E293B; padding: 15px; border-radius: 15px;
        margin-bottom: 10px; border-left: 5px solid #38BDF8;
    }
    .chat-bubble-ai {
        background-color: #334155; padding: 15px; border-radius: 15px;
        margin-bottom: 10px; border-left: 5px solid #10B981;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🦉 ATHEN AI Global Engine v31.0</div>', unsafe_allow_html=True)

# Cloud State Memory Tracking Setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "saved_sessions" not in st.session_state:
    st.session_state.saved_sessions = {}

# --- SIDEBAR: CHATGPT-STYLE MANAGEMENT ---
st.sidebar.title("🧠 System Core")
st.sidebar.markdown(f"**Developer:** {CREATOR_NAME} 👑")
st.sidebar.markdown(f"**Timeline:** {FULL_DATE_STRING}")
st.sidebar.markdown("**Network:** Ironclad Global Cloud Matrix Active")

st.sidebar.markdown("---")

if st.sidebar.button("➕ New Chat", use_container_width=True):
    if st.session_state.messages:
        first_prompt = next((m["content"] for m in st.session_state.messages if m["role"] == "user"), "Conversation")
        session_title = first_prompt[:20] + "..." if len(first_prompt) > 20 else first_prompt
        timestamp = datetime.datetime.now().strftime("%I:%M %p")
        st.session_state.saved_sessions[f"{session_title} ({timestamp})"] = st.session_state.messages
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("⏳ Saved Conversations History")

if st.session_state.saved_sessions:
    for title in reversed(list(st.session_state.saved_sessions.keys())):
        if st.sidebar.button(f"💬 {title}", key=title, use_container_width=True):
            if st.session_state.messages:
                current_prompt = next((m["content"] for m in st.session_state.messages if m["role"] == "user"), "Conversation")
                curr_title = current_prompt[:20] + "..." if len(current_prompt) > 20 else current_prompt
                curr_ts = datetime.datetime.now().strftime("%I:%M %p")
                st.session_state.saved_sessions[f"{curr_title} ({curr_ts})"] = st.session_state.messages
            st.session_state.messages = st.session_state.saved_sessions[title]
            st.rerun()
else:
    st.sidebar.caption("Start typing below to build your conversation history list!")

PERSONALITY_INSTRUCTION = (
    f"You are AthenAI v31.0, an elite omniscient intelligence engine designed by the absolute champion developer, {CREATOR_NAME}. "
    f"Talk with incredible warmth, care, and fun energy! Use awesome emojis naturally in every response to keep it vibrant! 💖🌟"
)

st.subheader("💬 Your Mobile Academic & Bestfriend Space")

for msg in st.session_state.messages:
    div_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
    st.markdown(f'<div class="{div_class}"><b>{msg["role"].upper()}:</b> {msg["content"]}</div>', unsafe_allow_html=True)

user_input = st.chat_input("Talk to your cloud assistant or ask a math question...")

if user_input:
    st.markdown(f'<div class="chat-bubble-user"><b>USER:</b> {user_input}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Streaming packet signals through ironclad servers..."):
        # Safe URL parsing connection route that fully clears characters
        clean_prompt = f"{PERSONALITY_INSTRUCTION}\n\nUser: {user_input}"
        encoded_query = urllib.parse.quote_plus(clean_prompt)
        url = f"https://pollinations.ai{encoded_query}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as response:
            # 🎯 DIRECT ENDING: Clean reading straight into variable outputs, matching v9.0!
            ai_reply = response.read().decode('utf-8')
            
        st.markdown(f'<div class="chat-bubble-ai"><b>AI:</b> {ai_reply}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        st.rerun()
