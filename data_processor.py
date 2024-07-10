from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import pickle
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key from environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load documents
with open('documents.pkl', 'rb') as f:
    documents = pickle.load(f)

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Generate embedding vectors for texts
embedding_vectors = embeddings.embed_documents([text.page_content for text in texts])

# Save processed data
with open('processed_data.pkl', 'wb') as f:
    pickle.dump({'texts': texts, 'embedding_vectors': embedding_vectors}, f)
