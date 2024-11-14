from flask import Flask, request, jsonify, render_template
import cohere

# Initialize Flask app
app = Flask(__name__)

# Initialize Cohere client with your API key
co = cohere.Client("45BpYDLVZcfKlgMGMiTAObC7GNdpNnAVHP4u5GXA")  # Replace with your actual Cohere API key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    # Get the user's message from the request
    user_message = request.json["message"]

    # Use Cohere's 'generate' endpoint to get a response
    response = co.generate(
        model='command-xlarge-nightly',  # Choose a suitable Cohere model
        prompt=f"You are a helpful assistant. Respond to the user's question: {user_message}",
        max_tokens=50  # Limit the response length
    )

    # Extract the generated response text
    bot_message = response.generations[0].text.strip()

    return jsonify({"response": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
