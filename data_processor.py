from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import pickle
import os

# Load documents
with open('documents.pkl', 'rb') as f:
    documents = pickle.load(f)

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Create embeddings
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
embeddings = OpenAIEmbeddings()

# Save processed data
with open('processed_data.pkl', 'wb') as f:
    pickle.dump({'texts': texts, 'embeddings': embeddings}, f)
