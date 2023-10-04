FROM langchain/langchain

WORKDIR /app

RUN pip install sentence_transformers

COPY test.py .

ENTRYPOINT ["python", "test.py"]
