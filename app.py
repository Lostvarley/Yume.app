from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# conecta com Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return "Yume IA online 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "Seu nome é Yume. Você é uma IA estilo anime, amigável, inteligente e divertida."},
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = "Erro: " + str(e)

    return jsonify({"response": reply})