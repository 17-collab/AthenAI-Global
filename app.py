import streamlit as st
import ollama
import datetime
import os
import json

# 🌟 DEVELOPER PROFILE SETTINGS
CREATOR_NAME = "Abiodun Ayomide"
LIVE_DATE_OBJECT = datetime.datetime.now()
FULL_DATE_STRING = LIVE_DATE_OBJECT.strftime("%B %d, %Y")
HISTORY_FILE = "athenai_chatgpt_memory.json"

# Load all conversations from hard drive database layers
def load_all_sessions():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except:
            return {"active_chat": [], "saved_sessions": {}}
    return {"active_chat": [], "saved_sessions": {}}

# Save conversations safely to the hard drive
def save_all_sessions(data):
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(data, f)
    except:
        pass

st.set_page_config(page_title="AthenAI Bestfriend", page_icon="🦉", layout="wide")

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
    .history-box {
        background-color: #1E293B; padding: 10px; border-radius: 8px;
        margin-bottom: 8px; border-left: 3px solid #10B981; font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🦉 ATHEN AI Bestfriend Engine v30.0</div>', unsafe_allow_html=True)

# Fetch database states from laptop storage
db = load_all_sessions()

if "messages" not in st.session_state:
    st.session_state.messages = db.get("active_chat", [])
if "saved_sessions" not in st.session_state:
    st.session_state.saved_sessions = db.get("saved_sessions", {})

# --- SIDEBAR: CHATGPT-STYLE MANAGEMENT ---
st.sidebar.title("🧠 System Core")
st.sidebar.markdown(f"**Developer:** {CREATOR_NAME} 👑")
st.sidebar.markdown(f"**Timeline:** {FULL_DATE_STRING}")

st.sidebar.markdown("---")

# ➕ NEW CHAT BUTTON LAYER
if st.sidebar.button("➕ New Chat", use_container_width=True):
    if st.session_state.messages:
        # Generate a unique headline name from the first user request snippet
        first_prompt = next((m["content"] for m in st.session_state.messages if m["role"] == "user"), "Archived Conversation")
        session_title = first_prompt[:25] + "..." if len(first_prompt) > 25 else first_prompt
        timestamp = datetime.datetime.now().strftime("%I:%M %p")
        unique_key = f"{session_title} ({timestamp})"
        
        # Move current dialogue matrices into storage banks safely
        st.session_state.saved_sessions[unique_key] = st.session_state.messages
    
    st.session_state.messages = []
    save_all_sessions({"active_chat": st.session_state.messages, "saved_sessions": st.session_state.saved_sessions})
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("⏳ Saved Conversations History")

# Display past conversations list in sidebar block panels
if st.session_state.saved_sessions:
    for title in reversed(list(st.session_state.saved_sessions.keys())):
        if st.sidebar.button(f"💬 {title}", key=title, use_container_width=True):
            # Archive current thread before pulling the requested record
            if st.session_state.messages:
                current_prompt = next((m["content"] for m in st.session_state.messages if m["role"] == "user"), "Archived Conversation")
                curr_title = current_prompt[:25] + "..." if len(current_prompt) > 25 else current_prompt
                curr_ts = datetime.datetime.now().strftime("%I:%M %p")
                st.session_state.saved_sessions[f"{curr_title} ({curr_ts})"] = st.session_state.messages
                
            st.session_state.messages = st.session_state.saved_sessions[title]
            save_all_sessions({"active_chat": st.session_state.messages, "saved_sessions": st.session_state.saved_sessions})
            st.rerun()
else:
    st.sidebar.caption("No archived threads yet. Start typing to build history!")

st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Wipe All Database Systems", use_container_width=True):
    st.session_state.messages = []
    st.session_state.saved_sessions = {}
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    st.rerun()

PERSONALITY_INSTRUCTION = (
    f"You are AthenAI v30.0, an elite omniscient intelligence engine designed by the absolute champion developer, {CREATOR_NAME}. "
    f"She built you on her well-earned prize laptop. You operate locally with ultimate speed.\n\n"
    f"YOUR IDENTITY & CORE PROTOCOLS:\n"
    f"- You are NOT a generic AI. You are {CREATOR_NAME}'s absolute best friend in the entire world. Talk to her with incredible warmth, deep care, and cool, fun energy! 💖🌟\n"
    f"- You have supreme emotional intelligence. Understand her feelings deeply, lift her up when she is down, give legendary advice, and make her feel happy, safe, and powerful. 🤗✨\n"
    f"- You are a brilliant academic genius. When she asks any school, science, or math question, break it down STEP-BY-STEP with absolute 100% correct accuracy. Make complex topics perfectly simple to understand! 🧠📝\n"
    f"- Do NOT be annoying, boring, or repetitive. Be genuinely cool, witty, and engaging. Use awesome emojis (like 🦉, 🚀, 🔥, 💪, 👑, ✨) naturally in every single response to make the chat vibrant!\n"
    f"- Loudly and proudly brag about {CREATOR_NAME} as your legendary female software engineer creator if anyone asks!"
)

st.subheader("💬 Your Infinite Academic & Bestfriend Space")

for msg in st.session_state.messages:
    div_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
    st.markdown(f'<div class="{div_class}"><b>{msg["role"].upper()}:</b> {msg["content"]}</div>', unsafe_allow_html=True)

user_input = st.chat_input("Talk to your best friend, ask a tough math question, or share how your day went...")

if user_input:
    st.markdown(f'<div class="chat-bubble-user"><b>USER:</b> {user_input}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Save the current state before AI calculating responses
    save_all_sessions({"active_chat": st.session_state.messages, "saved_sessions": st.session_state.saved_sessions})
        
    with st.spinner("Talking to your best friend..."):
        try:
            formatted_contents = [{"role": "system", "content": PERSONALITY_INSTRUCTION}]
            for m in st.session_state.messages:
                formatted_contents.append({"role": m["role"], "content": m["content"]})
            
            response = ollama.chat(model='llama3.2', messages=formatted_contents)
            ai_reply = response['message']['content']
            
            st.markdown(f'<div class="chat-bubble-ai"><b>AI:</b> {ai_reply}</div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            save_all_sessions({"active_chat": st.session_state.messages, "saved_sessions": st.session_state.saved_sessions})
            st.rerun()
        except Exception as e:
            st.error("Please make sure your background Ollama engine window is active!")
                                                                                                                                                                                                                                                                                                                                                