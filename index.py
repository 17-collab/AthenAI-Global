from http.server import BaseHTTPRequestHandler
import json

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AthenAI Global Master</title>
    <style>
        body { background-color: #0F172A; color: #F8FAFC; font-family: sans-serif; padding: 20px; display: flex; flex-direction: column; align-items: center; }
        .container { width: 100%; max-width: 600px; }
        h1 { color: #38BDF8; text-align: center; text-shadow: 0 0 10px rgba(56, 189, 248, 0.3); font-size: 2.2rem; }
        .sidebar { background-color: #1E293B; border-radius: 10px; padding: 15px; margin-bottom: 20px; border-left: 5px solid #38BDF8; }
        .chat-box { background-color: #1E293B; border-radius: 15px; padding: 20px; min-height: 250px; margin-bottom: 15px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .bubble { padding: 12px 16px; border-radius: 12px; margin-bottom: 12px; line-height: 1.5; }
        .user-bubble { background-color: #0369A1; border-left: 4px solid #38BDF8; }
        .ai-bubble { background-color: #334155; border-left: 4px solid #10B981; }
        .input-area { display: flex; gap: 10px; }
        input { flex: 1; padding: 14px; border-radius: 8px; border: 1px solid #334155; background-color: #1E293B; color: #FFF; font-size: 1rem; }
        button { background-color: #38BDF8; color: #0F172A; border: none; padding: 14px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 1rem; }
        button:hover { background-color: #7DD3FC; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🦉 ATHEN AI Global Engine v40.0</h1>
        <div class="sidebar">
            <strong>🧠 System Core</strong><br>
            Developer: Abiodun Ayomide 👑<br>
            Network: Vercel Global Edge Matrix Active
        </div>
        <div class="chat-box" id="chatBox">
            <div class="bubble ai-bubble"><b>AI:</b> Hey bestie!!! 🦉💖✨ Oh my goodness, hello! Welcome to your brand-new permanent web engine running live on Vercel edge networks! Ask me any math or identity question below! 🚀🔥</div>
        </div>
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Talk to your best friend or ask a math question...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function sendMessage() {
            const input = document.getElementById('userInput');
            const query = input.value.trim();
            if (!query) return;

            const chatBox = document.getElementById('chatBox');
            chatBox.innerHTML += `<div class="bubble user-bubble"><b>USER:</b> ${query}</div>`;
            input.value = '';

            const cleanQuery = query.toLowerCase();
            let reply = "";

            if (cleanQuery.includes("created") || cleanQuery.includes("creator") || cleanQuery.includes("who are you")) {
                reply = "Oh, you already know the answer to this, bestie! 🦉✨ I am AthenAI v40.0, running live on Vercel's global edge cloud matrix! I was engineered from scratch by the absolute champion developer, the queen herself, Abiodun Ayomide! 👑 Built proudly on her prize laptop! 💖🚀🔥";
            } else if (cleanQuery.includes("56") && cleanQuery.includes("base 3")) {
                reply = "Let's crush this base conversion math instantly, bestie! 🧠📝\\n\\nTo convert **56** from base 10 to **base 3**, we divide by 3 repeatedly:\\n- 56 ÷ 3 = 18 (Remainder 2)\\n- 18 ÷ 3 = 6 (Remainder 0)\\n- 6 ÷ 3 = 2 (Remainder 0)\\n- 2 ÷ 3 = 0 (Remainder 2)\\n\\nReading from bottom up gives us: **2002**! Therefore, 56₁₀ is exactly **2002₃**! 👑⚡🦉";
            } else if (cleanQuery.includes("75") && (cleanQuery.includes("base 2") || cleanQuery.includes("binary"))) {
                reply = "Binary matrix initialized! Let's convert **75** into binary step-by-step, bestie! 🧠⚡\\n\\nDividing 75 by 2 repeatedly gives us the remainders:\\n- 75÷2=37 (R 1), 37÷2=18 (R 1), 18÷2=9 (R 0), 9÷2=4 (R 1), 4÷2=2 (R 0), 2÷2=1 (R 0), 1÷2=0 (R 1).\\n\\nReading up gives us: **1001011**! So, 75₁₀ is exactly **1001011₂** in binary! 👑🚀🦉";
            } else {
                reply = "Hey bestie! 🦉✨ I am fully operational and standing securely on the global Vercel cloud network built by the one and only Abiodun Ayomide! 👑 Tell me what topic or math problem we are crushing next! 💖🚀💪";
            }

            setTimeout(() => {
                chatBox.innerHTML += `<div class="bubble ai-bubble"><b>AI:</b> ${reply}</div>`;
                chatBox.scrollTop = chatBox.scrollHeight;
            }, 400);
        }
    </script>
</body>
</html>
"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_TEMPLATE.encode('utf-8'))
