import random
import string
import re

# Knowledge Base
KNOWLEDGE_BASE = [
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "good morning"],
        "responses": [
            "Hello! Welcome to CollegeBot.",
            "Hi there! How can I help you?",
            "Hey! Ask me anything about the college."
        ]
    },

    {
        "tag": "admission",
        "patterns": ["admission", "apply", "enroll", "registration"],
        "responses": [
            "You can apply online through the college website.",
            "Admissions open every June."
        ]
    },

    {
        "tag": "fees",
        "patterns": ["fees", "fee structure", "cost", "tuition"],
        "responses": [
            "Engineering fees are Rs 80,000 per year.",
            "Fees vary depending on the course."
        ]
    },

    {
        "tag": "courses",
        "patterns": ["courses", "programs", "degrees", "subjects"],
        "responses": [
            "We offer B.Tech, BCA, BBA, MBA, MCA and more."
        ]
    },

    {
        "tag": "hostel",
        "patterns": ["hostel", "accommodation", "room"],
        "responses": [
            "Separate hostels are available for boys and girls."
        ]
    },

    {
        "tag": "placements",
        "patterns": ["placement", "job", "salary", "package"],
        "responses": [
            "Top recruiters include Infosys, TCS and Amazon."
        ]
    },

    {
        "tag": "thanks",
        "patterns": ["thanks", "thank you"],
        "responses": [
            "You're welcome!",
            "Happy to help!"
        ]
    },

    {
        "tag": "farewell",
        "patterns": ["bye", "goodbye", "exit", "quit"],
        "responses": [
            "Goodbye! Best of luck.",
            "Take care!"
        ]
    },

    {
        "tag": "unknown",
        "patterns": [],
        "responses": [
            "Sorry, I didn't understand that.",
            "Please ask about admissions, fees, hostel or placements."
        ]
    }
]

# Text Preprocessing
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

# Regex Patterns
REGEX_PATTERNS = [
    (r'\b(hi|hello|hey)\b', 'greeting'),
    (r'\b(admission|apply|enroll|registration)\b', 'admission'),
    (r'\b(fee|fees|cost|tuition)\b', 'fees'),
    (r'\b(course|courses|program|degree)\b', 'courses'),
    (r'\b(hostel|accommodation|room)\b', 'hostel'),
    (r'\b(placement|job|salary|package)\b', 'placements'),
    (r'\b(thanks|thank)\b', 'thanks'),
    (r'\b(bye|goodbye|exit|quit)\b', 'farewell')
]

# Find Response
def regex_match(user_input):
    cleaned = preprocess(user_input)

    for pattern, tag in REGEX_PATTERNS:
        if re.search(pattern, cleaned):
            for entry in KNOWLEDGE_BASE:
                if entry["tag"] == tag:
                    return tag, random.choice(entry["responses"])

    for entry in KNOWLEDGE_BASE:
        if entry["tag"] == "unknown":
            return "unknown", random.choice(entry["responses"])

# Main Chat Function
def chat():
    print("=" * 50)
    print("CollegeBot - AI College Assistant")
    print("=" * 50)
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        tag, response = regex_match(user_input)

        print("Bot:", response)

        if tag == "farewell":
            print("Session Ended.")
            break

# Run Program
if __name__ == "__main__":
    chat()