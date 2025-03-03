from transformers import pipeline

# Load a question-detection model
question_extractor = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Example LinkedIn post text
linkedin_text = """
I recently completed my AWS certification! What is the best way to get a cloud computing job?
Also, how can I network better with recruiters?
"""

# Detect questions
questions = []
for sentence in linkedin_text.split("."):
    if "?" in sentence:
        questions.append(sentence.strip())

print("Extracted Questions:", questions)
