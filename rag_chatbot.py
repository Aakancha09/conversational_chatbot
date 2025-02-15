#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import gradio as gr
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import ollama

# Function to load, split, and retrieve documents
def load_and_retrieve_docs(url):
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict()
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} documents")  # Debugging statement
    for doc in docs:
        print(doc.page_content[:500])  # Print the first 500 characters of each document
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    print(f"Created {len(splits)} document splits")  # Debugging statement
    for split in splits:
        print(split.page_content[:500])  # Print the first 500 characters of each split
    
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    print("Embeddings and vector store created successfully")  # Debugging statement
    
    return vectorstore.as_retriever()

# Function to format documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Function that defines the RAG chain
def rag_chain(url, question):
    retriever = load_and_retrieve_docs(url)
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']

# Gradio interface
iface = gr.Interface(
    fn=rag_chain,
    inputs=["text", "text"],
    outputs="text",
    title="RAG Chain Question Answering",
    description="Enter a URL and a query to get answers from the RAG chain."
)

# Launch the app
iface.launch()

