from flask import Flask, request, jsonify
from config import SYSTEM_PROMPT

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    prompt = f"{SYSTEM_PROMPT}\nUser: {user_input}"
    return jsonify({"prompt_used": prompt})

if __name__ == "__main__":
    app.run(debug=True)
