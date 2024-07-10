from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import pickle
import os

# Load environment variables
load_dotenv()

# Load documents
with open('documents.pkl', 'rb') as f:
    documents = pickle.load(f)

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Create embeddings for the chunks
openai_api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(api_key=openai_api_key)

# Save processed data with chunks and embeddings
with open('processed_data.pkl', 'wb') as f:
    pickle.dump({'texts': texts, 'embeddings': embeddings}, f)
