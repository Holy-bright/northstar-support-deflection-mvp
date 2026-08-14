from flask import Flask, render_template, request, jsonify
from chatbot import get_reply

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    return jsonify({"reply": get_reply(user_message)})


if __name__ == "__main__":
    app.run(debug=True)
