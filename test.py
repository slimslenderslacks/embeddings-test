# pip install langchain
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="/embedding_model"
)

texts = ["This is a test sentence."] * 100

sum = 0
count = 0
for text in texts:
    emb = embeddings.embed_query(text)
    sum = sum + len(emb)
    count = count + 1

print(sum, count)
