from transformers import pipeline

class Summarizer:

    def __init__(self):
        self.model = pipeline('summarization')


    def summarize(self, text):
        return self.model(text)[0]['summary_text']