import requests

def add_to_corpus(text):
    response = requests.post('http://ir-platform:8000/add_document', json={'text':text}).json()
    return response['text']


def retrieve_passage(query):
    # print(query)
    response = requests.post('http://ir-platform:8000/retrieve_passage', json={'text':query}).json()
    # print(response)
    return response['text']


def get_random_examples():
    response = requests.get('http://ir-platform:8000/random_documents').json()
    return response['texts']


def summarize(text):
    response = requests.post('http://ir-platform:8000/summary_text', json={'text': text}).json()
    return response['text']