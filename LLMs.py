# from transformers import pipeline

# classifier = pipeline("sentiment-analysis")



# result = classifier("I hate this class")

# print(result)


from transformers import pipeline


summarize = pipeline("summarization")

generator = pipeline(
    "text-generation",
    model="gpt2"
)

result = generator(
    "Artificial Intelligence is",
    max_new_tokens=50,     # instead of max_length
    do_sample=True,
    temperature=0.7,
    pad_token_id=50256
)

# print(result[0]["generated_text"])


summary = summarize(
  long_text,
  max_length=100
  min_length=30
)