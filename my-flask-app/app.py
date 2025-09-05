from flask import Flask, jsonify, request

app = Flask(__name__)

# Predefined unique emotional wishes
wishes = [
    "🌟 Happy Teacher’s Day! In the architecture of my career, you’re the hidden framework—clean logic, solid patterns, and humane design holding everything together 🏗️💻; thank you for teaching me to build with both rigor and heart ❤️🙏.",
    "🧭 If knowledge is a compass, your mentorship is true north—steady through bugs 🐞, deadlines ⏳, and doubt 🌌; grateful for the way you debugged my thinking 🧑‍💻 and refactored my courage 💪.",
    "🕯️ A great mentor is like a candle – lighting the way for others 🔦✨, burning selflessly to brighten paths.",
    "💡 You didn’t just transfer skills—you sparked wonder 🔥; every concept you taught became a bridge 🌉 from 'why' to 'wow.' 🌺 Happy Teacher’s Day to a mentor who makes complexity feel like poetry 🎶📖.",
    "📂 In the repository of my life, your commits are the ones that never need a rollback ♻️—thoughtful 🤝, future-proof 🔮, and full of tests for resilience 🛡️. Thank you for being my north-star maintainer 🌠.",
    "🔧 From spaghetti thoughts 🍝 to elegant architectures 🏛️, you taught me to separate concerns 📑, document kindness 💕, and ship with integrity 🚀; the pull requests you approved in me changed my roadmap 🗺️.",
    "📊 You turned failures into logs 📜, logs into insights 💡, and insights into growth 🌱🌳; thanks for teaching me that the best systems—and people—scale through patience ⏳ and practice 🏋️.",
    "⏸️ Your belief became my breakpoint—the moment everything paused ✨, made sense 🧘, and moved forward with purpose 🎯; thank you 🙏💖.",
    "🧩 Your wisdom is the design pattern I reach for when stakes are high ⛰️🔥—thank you, today and always 🌹.",
    "🌷 With deep gratitude for your steadfast mentorship 🙌, intellectual generosity 📚, and unwavering integrity 💎—thank you for illuminating complex paths 🌌 with clarity and care 🕊️."
]

wish_index = 0  # track which wish to show next

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Teachers' Day Chatbot 💻</title>
    <style>
      body { background: linear-gradient(135deg, #0b0b0d, #1a0f1d); font-family: "Segoe UI", sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
      .chat-container { background: #1a0f1d; width: 400px; height: 600px; border-radius: 15px; display: flex; flex-direction: column; box-shadow: 0 0 20px #ff4fd8; border: 1px solid #ff4fd8; }
      .header { background: #120916; color: #ff70ff; padding: 15px; text-align: center; font-weight: bold; font-size: 18px; border-bottom: 1px solid #ff4fd8; border-radius: 15px 15px 0 0; text-shadow: 0 0 10px #ff4fd8; }
      .chat-box { flex: 1; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; }
      .bot-message { align-self: flex-start; background: #ff4fd8; color: black; padding: 10px 15px; border-radius: 15px 15px 15px 0; max-width: 80%; box-shadow: 0 0 10px #ff4fd8; font-size: 14px; }
      .user-message { align-self: flex-end; background: #2b1a2e; color: #ff70ff; padding: 10px 15px; border-radius: 15px 15px 0 15px; max-width: 80%; box-shadow: 0 0 10px #3c103d; font-size: 14px; }
      .input-area { display: flex; padding: 10px; border-top: 1px solid #ff4fd8; }
      input { flex: 1; padding: 10px; border: none; border-radius: 20px; background: #120916; color: #ff70ff; font-size: 14px; outline: none; box-shadow: inset 0 0 8px #3c103d; }
      button { margin-left: 10px; padding: 10px 15px; border: none; border-radius: 20px; background: linear-gradient(135deg, #ff4fd8, #ff70ff); color: black; font-weight: bold; cursor: pointer; transition: 0.2s ease-in-out; box-shadow: 0 0 10px #ff4fd8; }
      button:hover { background: linear-gradient(135deg, #ff70ff, #ff4fd8); box-shadow: 0 0 20px #ff70ff; }
    </style>
  </head>
  <body>
    <div class="chat-container">
      <div class="header">💻 Teachers' Day Chatbot</div>
      <div class="chat-box" id="chatBox">
        <div class="bot-message">System Booting... Type anything to get a wish 💡</div>
      </div>
      <div class="input-area">
        <input id="userInput" placeholder="Type here..." />
        <button onclick="sendMessage()">Send</button>
      </div>
    </div>

    <script>
      function sendMessage() {
        let userText = document.getElementById("userInput").value;
        if (!userText.trim()) return;
        let chatBox = document.getElementById("chatBox");

        // Show user message
        let userMsg = document.createElement("div");
        userMsg.className = "user-message";
        userMsg.innerText = userText;
        chatBox.appendChild(userMsg);

        if (userText.toLowerCase() === "exit") {
          let botMsg = document.createElement("div");
          botMsg.className = "bot-message";
          botMsg.innerText = "Goodbye Mam ❤";
          chatBox.appendChild(botMsg);
        } else {
          fetch("/get_wish")
            .then(response => response.json())
            .then(data => {
              let botMsg = document.createElement("div");
              botMsg.className = "bot-message";
              botMsg.innerText = data.wish;
              chatBox.appendChild(botMsg);
              chatBox.scrollTop = chatBox.scrollHeight;
            });
        }

        document.getElementById("userInput").value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
      }
    </script>
  </body>
</html>
"""

@app.route("/get_wish")
def get_wish():
    global wish_index
    if wish_index < len(wishes):
        message = wishes[wish_index]
        wish_index += 1
    else:
        message = "🔄 Restarting wishes..."
        wish_index = 0
    return jsonify({"wish": message})

if __name__ == "__main__":
    app.run(debug=True)
