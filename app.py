from flask import Flask, request, send_from_directory, redirect, url_for, jsonify
import os
import socket
import threading
import webbrowser
import time

app = Flask(__name__)

# ---------------- CONFIG ----------------
PORT = 8000
USER_DIR = os.path.join(os.path.expanduser("~"), "Documents", "NetBridge")
os.makedirs(USER_DIR, exist_ok=True)

chat_messages = []

# ---------------- UTILS ----------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# ---------------- MAIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename:
            file.save(os.path.join(USER_DIR, file.filename))
        return redirect(url_for("index"))

    files = os.listdir(USER_DIR)
    file_html = ""

    for f in files:
        if f.lower().endswith(".mp4"):
            file_html += f"""
            <div class="card">
                <b>{f}</b><br>
                <video controls>
                    <source src="/stream/{f}" type="video/mp4">
                </video>
            </div>
            """
        else:
            file_html += f"""
            <div class="card">
                <a href="/download/{f}">{f}</a>
            </div>
            """

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>NetBridge</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    margin: 0;
}}
.container {{
    max-width: 900px;
    margin: auto;
    background: white;
    padding: 20px;
    margin-top: 20px;
    border-radius: 8px;
}}
h1 {{ color: #2c3e50; }}
.url {{
    background: #eef;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 15px;
}}
.card {{
    margin-bottom: 15px;
}}
video {{
    width: 100%;
    max-width: 400px;
    margin-top: 5px;
}}
.chat-box {{
    border: 1px solid #ccc;
    height: 200px;
    overflow-y: auto;
    padding: 10px;
    background: #fafafa;
    margin-bottom: 10px;
}}
.chat-input {{
    display: flex;
    gap: 10px;
}}
.chat-input input {{
    flex: 1;
    padding: 8px;
}}
button {{
    padding: 8px 15px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}}
button:hover {{
    background: #0056b3;
}}
</style>
</head>

<body>
<div class="container">
    <h1>NetBridge</h1>
    <p><b>Local Offline File Sharing, Streaming & LAN Chat Tool</b></p>

    <div class="url">
        <b>Open on mobile:</b><br>
        http://{get_local_ip()}:{PORT}
    </div>

    <h3>Upload File</h3>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <h3>Files</h3>
    {file_html}

    <h3>LAN Chat</h3>
    <div id="chat" class="chat-box"></div>

    <div class="chat-input">
        <input id="msg" placeholder="Type a message">
        <button onclick="sendMsg()">Send</button>
    </div>
</div>

<script>
function loadChat() {{
    fetch('/chat')
    .then(res => res.json())
    .then(data => {{
        let box = document.getElementById('chat');
        box.innerHTML = '';
        data.forEach(m => {{
            let d = document.createElement('div');
            d.textContent = m;
            box.appendChild(d);
        }});
        box.scrollTop = box.scrollHeight;
    }});
}}

function sendMsg() {{
    let msg = document.getElementById('msg').value;
    if (!msg.trim()) return;
    fetch('/send', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({{ message: msg }})
    }});
    document.getElementById('msg').value = '';
}}

setInterval(loadChat, 1000);
loadChat();
</script>
</body>
</html>
"""

# ---------------- FILE ROUTES ----------------
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(USER_DIR, filename, as_attachment=True)

@app.route("/stream/<filename>")
def stream(filename):
    return send_from_directory(USER_DIR, filename)

# ---------------- CHAT ROUTES ----------------
@app.route("/chat")
def chat():
    return jsonify(chat_messages)

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    if data and "message" in data:
        chat_messages.append(data["message"])
    return "OK"

# ---------------- LAUNCHER ----------------
def open_browser():
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    print("===================================")
    print(" NetBridge running")
    print(f" PC     : http://localhost:{PORT}")
    print(f" Mobile : http://{get_local_ip()}:{PORT}")
    print(f" Folder : {USER_DIR}")
    print("===================================")

    threading.Thread(target=open_browser).start()
    app.run(host="0.0.0.0", port=PORT)