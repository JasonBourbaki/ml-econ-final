import numpy as np
import pandas as pd
from BCEmbedding import EmbeddingModel

data = pd.read_csv('weibo_texts.csv', encoding='utf-8')

# list of sentences
sentences = data['text'].tolist()

# init embedding model
model = EmbeddingModel(model_name_or_path="maidalun1020/bce-embedding-base_v1")

# extract embeddings
embeddings = model.encode(sentences)

# export embeddings
dim = 768
dimensions = [str(x) for x in range(1, dim+1)]
dim_header = ['Dim' + d + '_texts' for d in dimensions]
df = pd.DataFrame(embeddings)
df.to_csv("embeddings.csv", header = dim_header)
