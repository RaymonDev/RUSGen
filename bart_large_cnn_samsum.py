


from transformers import pipeline
from tqdm import tqdm

def summarize(user_description: str):

    summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
    chunk_size = 1024  # Maximum sequence length supported by the model
    chunks = [user_description[i:i+chunk_size] for i in range(0, len(user_description), chunk_size)]
    summaries = []
    print("Summarizing...")
    for chunk in tqdm(chunks):
        summary = summarizer(chunk)[0]['summary_text']
        summaries.append(summary)
    return " ".join(summaries)
