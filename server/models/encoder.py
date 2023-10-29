from sentence_transformers import SentenceTransformer

class Encoder:
    def __init__(self, model):
        self.model = SentenceTransformer(model)

    def encode(self, corpus, bsize=64):        
        encoded_data = self.model.encode(corpus, batch_size=bsize, show_progress_bar=True)
        return encoded_data