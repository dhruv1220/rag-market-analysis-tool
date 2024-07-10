# Market Intelligence Assistant

This project is a Market Intelligence Assistant that leverages Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) techniques to gather, process, and analyze market-related data from various sources. The assistant is designed to provide insights on market trends, competitor analysis, and other business intelligence tasks.

## Project Structure

The project is organized into the following main components:

- `data_collector.py`: Script to collect data from various web sources.
- `data_processor.py`: Script to process the collected data, split it into chunks, and create embeddings.
- `retriever.py`: Script to create a FAISS index for efficient retrieval.
- `llm_interface.py`: Script to integrate with OpenAI's GPT-4 for generating answers based on retrieved data.
- `main.py`: Main script to interact with the Market Intelligence Assistant.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dhruv1220/rag-market-analysis-tool.git
   cd rag-market-analysis-tool
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   USER_AGENT=your-user-agent-string
   ```

## Usage

### 1. Data Collection

Run the `data_collector.py` script to collect data from various web sources:
```bash
python data_collector.py
```

### 2. Data Processing

Run the `data_processor.py` script to process the collected data, split it into chunks, and create embeddings:
```bash
python data_processor.py
```

### 3. Create Retrieval System

Run the `retriever.py` script to create a FAISS index for efficient retrieval:
```bash
python retriever.py
```

### 4. Interact with the Assistant

Run the `main.py` script to interact with the Market Intelligence Assistant:
```bash
python main.py
```

### Example Questions

- "What are Apple's main competitors in the smartphone market?"
- "How does Apple's market share in tablets compare to other companies?"
- "What are the key features of Apple's latest iPhone model?"
- "How has Apple's services revenue grown in recent years?"
- "What are the main challenges Apple faces in the global market?"

## Project Components

### `data_collector.py`

This script collects data from specified web sources using `langchain_community.document_loaders.WebBaseLoader`. The collected documents are saved in a pickle file.

### `data_processor.py`

This script processes the collected data by splitting it into manageable chunks using `langchain.text_splitter.RecursiveCharacterTextSplitter` and creating embeddings using `langchain_openai.OpenAIEmbeddings`. The processed data is saved in a pickle file.

### `retriever.py`

This script creates a FAISS index for efficient data retrieval from the processed embeddings and saves the vectorstore in a pickle file.

### `llm_interface.py`

This script integrates with OpenAI's GPT-4 using `langchain.chat_models.ChatOpenAI` to generate answers based on the retrieved data. The retrieval and generation process is defined using `langchain.chains.RetrievalQA`.

### `main.py`

This script provides a simple command-line interface to interact with the Market Intelligence Assistant. Users can ask questions and receive answers based on the processed data.