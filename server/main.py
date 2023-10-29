from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
import json
import logging

from transformers import pipeline
from server_logic import LogicInstance

logger = logging.getLogger(__name__)


class RequestItemSingleText(BaseModel):
    text: str

class RequestItem(BaseModel):
    texts: list


logic_instance = LogicInstance()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Server setup. It can take a while...')   
    
    logic_instance = LogicInstance()
    logic_instance.load_and_index_corpus()

    yield
    logger.info('Server closed')
    logic_instance = None

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Information Retrieval platform"}


@app.post("/add_document")
async def add_document(item: RequestItemSingleText):
    logic_instance.add_document_to_db(item.text)


    return {'text': 'Documend added'}


@app.post("/retrieve_passage")
async def detect_language(item: RequestItemSingleText):
    passage = logic_instance.retrieve_passage(item.text)
  
    return {'text': passage}


@app.get('/random_documents')
async def get_random_documents():
    passages = logic_instance.get_example_data_from_corpus()

    return {'texts': passages}


@app.post('/summary_text')
async def summary_text(item: RequestItemSingleText):
    summary = logic_instance.summary_text(item.text)

    return {'text': summary}