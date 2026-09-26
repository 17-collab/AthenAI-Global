import streamlit as st
import datetime
import urllib.request
import json

# 🌟 DEVELOPER PROFILE SETTINGS
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
    .history-item {
        background-color: #1E293B; padding: 8px; border-radius: 5px;
        margin-bottom: 5px; font-size: 0.9rem; border-left: 3px solid #38BDF8;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🦉 ATHEN AI Global Engine v30.0</div>', unsafe_allow_html=True)

# Cloud Session Memory State Handling (No local hard-drive writes)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "saved_sessions" not in st.session_state:
    st.session_state.saved_sessions = {}

# --- SIDEBAR: CHATGPT-STYLE MANAGEMENT ---
st.sidebar.title("🧠 System Core")
st.sidebar.markdown(f"**Developer:** {CREATOR_NAME} 👑")
st.sidebar.markdown(f"**Timeline:** {FULL_DATE_STRING}")
st.sidebar.markdown("**Network:** Ironclad Global Cloud Matrix")

st.sidebar.markdown("---")

# ➕ NEW CHAT BUTTON TRACKER
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
    f"You are AthenAI v30.0, an elite omniscient intelligence engine designed by the absolute champion developer, {CREATOR_NAME}. "
    f"She built you on her well-earned prize laptop. You run on global cloud matrices. Talk with incredible warmth, care, and fun energy! 💖🌟\n\n"
    f"CORE PROTOCOLS:\n"
    f"- You are {CREATOR_NAME}'s absolute best friend in the world. Understand her feelings deeply, give legendary life advice, and make her happy. 🤗✨\n"
    f"- You are a brilliant academic genius. Break down math and science questions STEP-BY-STEP with absolute 100% correct accuracy. 🧠📝\n"
    f"- Use awesome emojis (like 🦉, 🚀, 🔥, 💪, 👑, ✨) naturally in every response to keep it vibrant!\n"
    f"- Brag passionately about {CREATOR_NAME} as your legendary female software engineer creator if asked!"
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
        url = "https://pollinations.ai"
        
        full_prompt = f"System Guideline: {PERSONALITY_INSTRUCTION}\n\nUser Dialogue Session:\n"
        for m in st.session_state.messages:
            full_prompt += f"{m['role'].upper()}: {m['content']}\n"
        
        # Enclose everything safely inside a clean data payload string to match Version 30.0 exactly
        payload = json.dumps({"messages": [{"role": "user", "content": full_prompt}]}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=20) as response:
            ai_reply = response.read().decode('utf-8')
            
        st.markdown(f'<div class="chat-bubble-ai"><b>AI:</b> {ai_reply}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        st.rerun()
