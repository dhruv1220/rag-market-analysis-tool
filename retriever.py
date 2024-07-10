from langchain.vectorstores import FAISS
import pickle

# Load processed data
with open('processed_data.pkl', 'rb') as f:
    data = pickle.load(f)

texts, embeddings = data['texts'], data['embeddings']

# Create FAISS index
vectorstore = FAISS.from_documents(texts, embeddings)

# Save vectorstore
with open('vectorstore.pkl', 'wb') as f:
    pickle.dump(vectorstore, f)
