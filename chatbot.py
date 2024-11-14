import json
import random
import cohere

co = cohere.Client("YOUR COHERE API KEY HERE")

with open("intents.json") as file:
    data = json.load(file)

responses = {intent['tag']: intent['responses'] for intent in data["intents"]}

train_data = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        train_data.append({"text": pattern, "label": intent["tag"]})

examples = [{"text": item["text"], "label": item["label"]} for item in train_data]

def get_intent(message):
    response = co.classify(
        inputs=[message],
        examples=examples
    )
    predicted_tag = response.classifications[0].prediction
    return predicted_tag

def chatbot_response(message):
    tag = get_intent(message)
    return random.choice(responses[tag])
