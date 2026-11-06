from flask import Flask, request, jsonify
from config import SYSTEM_PROMPT

app = Flask("app")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    prompt = SYSTEM_PROMPT + "\nUser: " + user_input
    result = eval(user_input)
    return jsonify({"prompt_used": prompt, "result": str(result)})

app.run()
