from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Distance, VectorParams, HnswConfig
from qdrant_client.models import SearchRequest
import json
from tqdm import tqdm
import time
import os
import logging

logger = logging.getLogger(__name__)


class QdrantInstance:

    def __init__(self, vector_size, collection_name):
        self.vector_size = vector_size
        self.collection_name = collection_name

        self.global_index=0

    def create_index(self, index_type):
        self.qdrantclient = QdrantClient(index_type, timeout=100000)

        self.index_type = index_type

        self.qdrantclient.recreate_collection(
            collection_name=self.collection_name, 
            vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE),
            )


    def load_index(self, index_type):
        self.index_type = index_type
        self.qdrantclient = QdrantClient(index_type)

    
    def encode_corpus(self, vectors, corpus):


        logging.info('Encoding corpus')
        corpus_payload = [{'text': i} for i in corpus]


        self.qdrantclient.upload_records(
	    collection_name=self.collection_name,
	    records=[
		    models.Record(
			    id=doc_num+self.global_index,
			    vector=vectors[doc_num],
			    payload=corpus_payload[doc_num]
		    ) for doc_num in range(len(corpus))
	        ]
        )

        self.global_index+=len(corpus)


    def add_to_collection(self, vector, text):
        self.qdrantclient.upload_records(
	    collection_name=self.collection_name,
	    records=[
		    models.Record(
			    id=self.global_index,
			    vector=vector,
			    payload={'text': text}
		    )
	        ]
        )


    def search(self, query_vector):

        retrieved = self.qdrantclient.search(query_vector=query_vector,
                collection_name=self.collection_name,
                with_vectors=False,
                limit=5)
        
        return [(i.payload['text'], i.score) for i in retrieved]

