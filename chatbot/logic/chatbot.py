# chatbot/logic/chatbot_logic.py
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
predefined_queries = ["What is your name?", "How are you?", "Tell me a joke"]

vectorizer = TfidfVectorizer()
query_vectors = vectorizer.fit_transform(predefined_queries)

def handle_input(user_input):
    if isinstance(user_input, str):
        response = chatbot(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
    elif isinstance(user_input, list):
        response = "Button response: " + user_input[0]
    else:
        response = "Sorry, I didn't understand that input."
    return response

def find_nearest_query(user_input):
    input_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(input_vector, query_vectors)
    most_similar_index = similarities.argmax()
    return predefined_queries[most_similar_index]

def handle_input_with_fallback(user_input):
    response = handle_input(user_input)
    if "Sorry, I didn't understand that input." in response:
        nearest_query = find_nearest_query(user_input)
        response = "Did you mean: " + nearest_query
    return response
