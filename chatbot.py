import json
import random
import cohere

# Initialize Cohere with API key
co = cohere.Client("45BpYDLVZcfKlgMGMiTAObC7GNdpNnAVHP4u5GXA")  # replace with your Cohere API key

# Load intents and responses from intents.json
with open("intents.json") as file:
    data = json.load(file)

# Map each tag to its respective responses
responses = {intent['tag']: intent['responses'] for intent in data["intents"]}

# Prepare the training data for Cohere's classification
train_data = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        train_data.append({"text": pattern, "label": intent["tag"]})

# Convert to Cohere format for classify endpoint
examples = [{"text": item["text"], "label": item["label"]} for item in train_data]

# Define a function to get intent prediction from Cohere's classify model
def get_intent(message):
    response = co.classify(
        inputs=[message],
        examples=examples
    )
    predicted_tag = response.classifications[0].prediction  # Predicted intent tag
    return predicted_tag

# Define a function to generate a chatbot response based on the intent
def chatbot_response(message):
    # Get the intent for the message
    tag = get_intent(message)
    
    # Select a random response associated with the identified intent tag
    return random.choice(responses[tag])
