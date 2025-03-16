from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List, Any

def build_vectorstore_retriever(
    urls: List[str],
    chunk_size: int = 1000,
    chunk_overlap: int = 100,
    embedding_model: str = "all-MiniLM-L6-v2"
) ->  Any :
    """
    Given a list of URLs, this function loads the documents from the URLs,
    splits the documents into chunks, builds a FAISS vector store using 
    HuggingFaceEmbeddings, and returns a retriever interface.

    Parameters:
        urls (List[str]): A list of URLs to load documents from.
        chunk_size (int): The maximum chunk size for text splitting.
        chunk_overlap (int): The number of overlapping characters between chunks.
        embedding_model (str): The name of the HuggingFace embedding model.

    Returns:
        retriever: A retriever interface from the FAISS vector store.
    """
    # Load documents from the provided URLs
    docs = [WebBaseLoader(url).load() for url in urls]
    # Flatten the list of documents (each WebBaseLoader returns a list of documents)
    docs_list = [item for sublist in docs for item in sublist]
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    doc_splits = text_splitter.split_documents(docs_list)
    
    # Create a FAISS vector store using the specified HuggingFace model for embeddings
    vectorstore = FAISS.from_documents(
        documents=doc_splits,
        embedding=HuggingFaceEmbeddings(model_name=embedding_model)
    )
    
    # Return a retriever object
    return vectorstore.as_retriever()