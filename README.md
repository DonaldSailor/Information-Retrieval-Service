# Information-Retrieval-Service

The project provides a simple demo of an Information Retrieval Platform
<br>
To run the project, first execute:
``` docker compose up```
Then run
``` localhost:8501/ ```

## Details

The project consists of a server and a Streamlit client connected through a REST API using the FastAPI library. The server utilizes a vector database called Qdrant and a bi-encoder model from the sentence-transformers library. Additionally, it enables the summarization of extracted texts using a model from the transformers library. <br>

Upon server startup, it loads and encodes 256 texts from the Scifact dataset from the [Beir Benchmark](!https://github.com/beir-cellar/beir) for the purpose of demonstrating its functionality.

### Config

The 'config.json' file in the 'server' directory allows for the modification of parameters and base models.

### Technologies 

| Technologies |
|------------------|
| Python   |
| Huggingface  |
| Sentence Transfermers  |
| Qdrant |
| FastAPI |
| Streamlit | 
| Docker | 

### Models

| Task | Model |
|------------------|------------------|
| Information Retrieval | [all-MiniLM-L6-v2](!https://www.sbert.net/docs/pretrained_models.html) |
| Summarization | [facebook/bart-large-cnn](!https://huggingface.co/facebook/bart-large-cnn) |