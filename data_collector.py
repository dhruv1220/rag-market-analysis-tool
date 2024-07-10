from langchain.document_loaders import WebBaseLoader

urls = [
    "https://www.apple.com/newsroom/",
    "https://www.samsung.com/us/news/",
    # Add more relevant URLs
]

loader = WebBaseLoader(urls)
documents = loader.load()

# Save documents to a file
import pickle
with open('documents.pkl', 'wb') as f:
    pickle.dump(documents, f)
