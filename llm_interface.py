from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import pickle

# Load vectorstore
with open('vectorstore.pkl', 'rb') as f:
    vectorstore = pickle.load(f)

# Set up LLM
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Create prompt template
template = """You are an AI assistant specializing in market intelligence for Apple Inc. Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer: """

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# Set up retrieval chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": prompt}
)

def get_answer(question):
    return chain.run(question)
