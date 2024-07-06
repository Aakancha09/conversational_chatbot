# conversational_chatbot
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RAG Chain Question Answering</title>
</head>
<body>
<h1>RAG Chain Question Answering</h1>

<p>This project implements a Question Answering (QA) system using a Retriever-Augmenter-Generator (RAG) chain architecture. It leverages the power of Ollama's Llama3 large language model (LLM) to answer your questions based on information retrieved from webpages.</p>

<h2>Features</h2>

<ul>
<li>Retrieves relevant information from webpages using document retrieval techniques.</li>
<li>Generates answers using Ollama's pre-trained Llama3 LLM.</li>
<li>Provides a user-friendly interface built with Gradio.</li>
</ul>

<h2>Getting Started</h2>

<p>To use this application, you'll need to install the required dependencies first.</p>

<h3>Installation</h3>

<pre>pip install gradio langchain langchain-community ollama</pre>

<h3>Running the application</h3>

<pre>python app.py</pre>

This will launch the Gradio interface at web browser.

<h2>Usage</h2>

<ol>
<li>Enter a URL in the first text box.</li>
<li>Enter your question in the second text box.</li>
<li>Click "Run" to get an answer based on the information retrieved from the webpage.</li>
</ol>

<h2>Technical Details</h2>

<p>The code utilizes the following libraries:</p>

<ul>
<li>Gradio: for building the user interface.</li>
<li>Langchain: for document loading and splitting.</li>
<li>Langchain Community: for pre-trained vector store and embeddings.</li>
<li>Ollama: for text generation with the Llama3 large language model.</li>
</ul>

<p>The application follows a RAG chain workflow:</p>

<ul>
<li>The load_and_retrieve_docs function retrieves relevant documents from the provided URL and creates a vector store for efficient information retrieval.</li>
<li>The format_docs function formats retrieved documents for better readability.</li>
<li>The rag_chain function defines the core RAG functionality. It retrieves relevant documents, formats the context with the question, and utilizes Ollama's Llama3 LLM to generate an answer based on the retrieved information and the user's question.</li>
</ul>

<h2>Further Enhancements</h2>

<ul>
<li>Implement error handling for invalid URLs or unsupported content types.</li>
<li>Integrate additional pre-processing steps for improved document cleaning and text normalization.</li>
<li>Explore different retrieval and generation models to potentially improve performance.</li>
</ul>

<h2>License</h2>

<h2>Contributing</h2>

We welcome contributions to this project. Please feel free to fork the repository and submit pull requests for any improvements or bug fixes.

</body>
</html>
