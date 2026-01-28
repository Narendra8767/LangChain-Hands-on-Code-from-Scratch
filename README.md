# 🔗 LangChain – Hands-on Code from Scratch

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Models-yellow?style=for-the-badge&logo=huggingface)
![ChromaDB](https://img.shields.io/badge/Chroma-Vector%20DB-purple?style=for-the-badge)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-red?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)
![GitHub](https://img.shields.io/badge/GitHub-Code%20Repository-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)


A complete, structured, hands-on LangChain playlist covering everything from LLMs & embeddings to chains, runnables, retrievers, vector stores, tools, and RAG systems.

This repository is designed to help you learn LangChain practically, step by step, with clean Python scripts and Jupyter notebooks.


##  What I Learn

- LangChain core concepts with from-scratch implementations  
- Chat models, embeddings, prompts, and structured outputs  
- Output parsers (JSON, Pydantic, Structured)  
- Chains & Runnables (Sequential, Parallel, Conditional, Branch)  
- Document loaders & text splitters  
- Vector stores & retrievers  
- Tool calling & custom tools  
- End-to-end RAG (Retrieval Augmented Generation) chatbot  


##  Key Concepts Covered

###  Chat Models
- Hugging Face chat models  
- Prompt → LLM → Response pipeline  

###  Embeddings
- Text embeddings using Hugging Face  
- Document similarity search  

###  Prompt Engineering
- Prompt templates  
- Message roles & placeholders  
- Chat history handling  

###  Structured Outputs
- TypedDict outputs  
- Pydantic-based structured responses  
- JSON schema outputs  

###  Output Parsers
- String output parser  
- JSON output parser  
- Pydantic & structured parsers  

###  Chains
- Simple chain  
- Sequential chain  
- Parallel chain  
- Conditional chain  

###  Runnables
- RunnableSequence  
- RunnableParallel  
- RunnablePassthrough  
- RunnableLambda  
- RunnableBranch  

###  Document Loaders
- Text files  
- PDF documents  
- Directory loaders  
- Web-based loaders  

###  Text Splitters
- Length-based splitting  
- Structure-based splitting  
- Python code splitter  
- Semantic meaning-based splitter  

###  Vector Stores & Retrievers
- Chroma vector store  
- Wikipedia retriever  
- Embedding-based retrieval  

###  Tools & Tool Calling
- Built-in LangChain tools  
- Custom tool creation  
- LLM tool calling  

###  RAG (Retrieval Augmented Generation)
- End-to-end RAG pipeline  
- YouTube / document-based chatbot  
- Vector store + retriever + LLM  


##  Tech Stack

- **Language:** Python  
- **Framework:** LangChain   
- **LLMs:** Hugging Face Models  
- **Vector DB:** Chroma  
- **Validation:** Pydantic  
- **Environment:** Jupyter Notebook & Python Scripts  

##  Credits & Acknowledgement

A big thanks to **CampusX (Nitish Singh)** 
for creating an amazing LangChain learning playlist and inspiring this hands-on implementation.

##  Connect

If you found this repository helpful   
Feel free to fork, star, and contribute!

## Repository Structure
LangChain-Hands-on-Code-from-Scratch/
│
├── 2_chatmodels/
│   └── 1_chatmodel_hf.py
│
├── 3_embedding/
│   ├── 1_embedding_hf.py
│   └── 2_document_similarity.py
│
├── 4_prompt/
│   ├── 1_prompt_ui.py
│   ├── 2_prompt_generator.py
│   ├── 3_chatbot.py
│   ├── 4_message_type.py
│   ├── 5_chat_prompt_template.py
│   ├── 6_chat_history.txt
│   ├── 7_message_placeholder.py
│   └── template.json
│
├── 5_structured_output/
│   ├── 1_typeddict_demo.py
│   ├── 2_typeddict_with_structured_output.py
│   ├── 3_with_structured_output_pydantic.py
│   ├── 4_pydantic_demo.py
│   ├── 5_json_schema.json
│   └── 6_with_structured_output_json.py
│
├── 6_output_parsers/
│   ├── 1_str_output_parser_demo.py
│   ├── 2_str_output_parser_using_chain.py
│   ├── 3_json_output_parser.py
│   ├── 4_structured_output_parser.py
│   └── 5_pydantic_output_parser.py
│
├── 7_chain/
│   ├── 1_simple_chain.py
│   ├── 2_sequential_chain.py
│   ├── 3_parallel_chain.py
│   └── 4_conditional_chain.py
│
├── 8_Runnables/
│   ├── 1_runnable_sequence.py
│   ├── 2_runnable_parallel.py
│   ├── 3_runnable_passthrough.py
│   ├── 4_runnable_lambda.py
│   └── 5_runnable_branch.py
│
├── 9_document_loader/
│   ├── books/
│   ├── 1_text_loader.py
│   ├── 2_pdf_loader.py
│   ├── 3_directory_loader.py
│   ├── 4_webbase_loader.py
│   ├── AB_de.txt
│   └── dl-curriculum.pdf
│
├── 10_text_splitters/
│   ├── 1_length_based.py
│   ├── 2_text_structure_based.py
│   ├── 3_python_code_splitter.py
│   └── 4_semantics_meaning_based.py
│
├── 11_vector_store/
│   └── my_chroma_db/
│       └── 1_vector_store_chroma.ipynb
│
├── 12_Retrievers/
│   └── 1_wikipedia_retriever.ipynb
│
├── 13_youtube_chatbot/
│   └── 1_RAG_using_langchain.ipynb
│
├── 14_Tools/
│   ├── 1_builtin_tools.ipynb
│   ├── 2_custom_tools.ipynb
│   ├── 3_tool_calling.ipynb
│   └── demo.py
│
├── .env
├── requirements.txt
└── README.md

