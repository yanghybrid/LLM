from transformers import pipeline

qa_model = pipeline("text-generation", model="deepseek-ai/deepseek-coder-7b")

for question in questions:
    answer = qa_model(question, max_length=100)
    print(f"Q: {question}\nA: {answer[0]['generated_text']}\n")
