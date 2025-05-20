# 🎓 Generative Search on College Website

This project implements a **Retrieval-Augmented Generation (RAG)** system titled **"Generative Search on College Website"**, built specifically to enhance search and QA capabilities using a college-related PDF document. It utilizes modern LLMs, vector databases, and an interactive frontend to provide context-aware, document-grounded answers.

---

##  Project Overview

- This system allows users to ask natural language questions related to the college's academic or administrative details by using a PDF document (such as a college handbook or syllabus).
- It integrates **LangChain** and **FAISS** for retrieval, **OpenAI's** embedding & language models, and **Reflex** for the frontend and interaction handling.

---

## 🧠 Features

- **RAG Pipeline** with FAISS vector search
- **OpenAI Embeddings + GPT models**
- **LangChain** orchestration with Conversational Memory
- **Frontend in Reflex** using [Reflex official Chat Template]
- Asynchronous UI interaction
- Optional Baidu API integration (for multilingual / alternative LLMs)
- Experimental support for **Pinecone** and **FireworksAI**

---

## 🛠️ Tech Stack

| Component      | Tech Used                                      |
|----------------|------------------------------------------------|
| Language Model | OpenAI GPT-3.5 Turbo, Cohere (optional)        |
| Embeddings     | OpenAI Embeddings, Cohere Embeddings (optional)|
| Vector DB      | FAISS (default), Pinecone (optional)           |
| Frameworks     | LangChain, Reflex (formerly Pynecone)          |
| PDF Parsing    | LangChain’s PyPDFLoader                        |
| UI             | Reflex + Chat Template                         |

---

## 📂 Data

- PDF document (`new244.pdf`) – The source file loaded and chunked using LangChain

---

## 🔍 How It Works

1. **PDF Loading**: Loads the PDF document using `PyPDFLoader`.
2. **Text Splitting**: Uses `RecursiveCharacterTextSplitter` to split into manageable chunks.
3. **Vectorization**: Each chunk is embedded using OpenAI or Cohere embeddings and stored in FAISS.
4. **Retrieval**: A `ConversationalRetrievalChain` is created using a retriever that fetches top-k similar chunks for any question.
5. **LLM Response**: OpenAI's `ChatOpenAI` generates a response using the retrieved context and recent chat history.
6. **Frontend**: The Reflex app UI handles questions, answers, chat context, and dynamic updates.

---

## 🖼️ Reflex Chat UI

This project uses the **Reflex Chat Template** for building an elegant and responsive frontend for the chatbot. Huge thanks to the Reflex team for providing this starter!

---

## 📦 Installation & Running

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**

   ```bash
   export OPENAI_API_KEY="your-api-key"
   export COHERE_API_KEY="your-cohere-key"  # optional
   export FIREWORKS_API_KEY="your-fireworks-key"  # optional
   ```

3. **Run the Reflex App**

   ```bash
   reflex run
   ```

---

## 🧪 Sample Query

> *"What is the eligibility criteria for the B.Tech program?"*

The system fetches relevant sections from the college PDF and responds accurately based on that data.

---

## 📜 License & Credits

- Reflex Chat UI powered by [Reflex Chat Template](https://github.com/reflex-dev/reflex-chat-template)
- Developed as part of an academic initiative to integrate AI with internal college systems
- LLM API usage courtesy of OpenAI, Cohere, and Baidu (optional)

---

## 🙌 Author

**Nandhu S Kumar**  
BTech in Computer Science and Engineering – College of Engineering Perumon  
> Passionate about building intelligent systems with real-world applications.
