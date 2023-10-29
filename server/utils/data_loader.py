from tqdm.autonotebook import tqdm
import json
import logging

logger = logging.getLogger(__name__)


def load_corpus(data_path):
    num_lines = sum(1 for i in open(data_path, 'rb'))
    corpus = []
    logger.info("Loading Corpus...")
    with open(data_path, encoding='utf8') as fIn:
        for line in tqdm(fIn, total=num_lines):    
            line = json.loads(line)
            corpus.append(line.get("text"))
    logger.info("Loaded %d Documents.", len(corpus))
    return corpus