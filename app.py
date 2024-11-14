from flask import Flask, request, jsonify, render_template
import cohere

app = Flask(__name__)
co = cohere.Client("YOUR COHERE API KEY HERE")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json["message"]
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=f"You are a helpful assistant. Respond to the user's question: {user_message}",
        max_tokens=50
    )
    bot_message = response.generations[0].text.strip()
    return jsonify({"response": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
