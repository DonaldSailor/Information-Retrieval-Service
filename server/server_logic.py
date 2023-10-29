import json

import utils.data_loader as dl
from models.encoder import Encoder
from models.summary_model import Summarizer
from vector_databases.qdrant_instance import QdrantInstance

import string
import random


class LogicInstance:
    
    def __init__(self):
        with open('config.json', 'r') as f:
            self.config=json.load(f)
        self.encoder = Encoder(self.config.get('models').get('encoder_model'))
        self.summarizer = Summarizer()
        self.qdrant_collection = self.config.get('qdrant').get('collection_name')
        self.qdrant_host = self.config.get('qdrant').get('host')
        self.vector_db = QdrantInstance(self.config.get('models').get('encoder_vector_size'),
                                        self.qdrant_collection)
        self.vector_db.create_index(self.qdrant_host)


    def load_and_index_corpus(self):
        corpus = dl.load_corpus(self.config.get('data').get('example_corpus'))[:self.config.get('data').get('examples_to_load')]
        encoded = self.encoder.encode(corpus)
        self.vector_db.encode_corpus(encoded, corpus)


    def add_document_to_db(self, text):
        encoding = self.encoder.encode(text)
        self.vector_db.add_to_collection(encoding, text)


    def retrieve_passage(self, text):
        encoding = self.encoder.encode(text)
        top_1 = self.vector_db.search(encoding)
        return top_1[0][0]


    def summary_text(self, text):
        summary = self.summarizer.summarize(text)
        return summary

    
    def get_example_data_from_corpus(self):
        random_query = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=30))
        encoding = self.encoder.encode(random_query)
        random_5 = self.vector_db.search(encoding)

        return [i[0] for i in random_5]


    def get_number_of_documents(self):
        return self.vector_db.get_number_of_documents()