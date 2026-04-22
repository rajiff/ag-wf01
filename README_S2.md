# Agentic AI Workflow (From Scratch)

## 📌 Overview

This project is a **from-scratch implementation of an Agentic AI system**, built incrementally to understand:

* Agent orchestration patterns
* Tool abstraction and extensibility
* Retrieval-Augmented Generation (RAG)
* Reasoning loops and decision-making
* Enterprise-grade system design principles

The goal is to evolve from a **minimal working system** to a **production-grade agent architecture**, following disciplined engineering practices.

---

## 🧠 Current Stage

**Step 2: LLM + RAG Integration (Foundational Agent System)**

### ✅ Implemented

* LLM integration (local via Ollama)
* Persistent vector store (ChromaDB)
* Document ingestion pipeline
* Embedding-based retrieval
* Retrieval as a Tool abstraction
* Context-aware response generation (RAG)

👉 The system can now answer questions grounded in provided documents.

---

## 🏗️ Project Structure

```
agentic-ai/
│
├── app.py
│
├── agent/
│   ├── base.py
│   └── simple_agent.py
│
├── llm/
│   ├── base.py
│   └── local_llm.py
│
├── tools/
│   ├── base.py
│   └── retrieval_tool.py
│
├── rag/
│   ├── ingest.py
│   └── retriever.py
│
├── models/
│   └── message.py
│
├── config/
│   └── settings.py
│
├── data/
│   └── docs.txt
│
├── chroma_db/          # Persistent vector database
│
├── requirements.txt
└── pyproject.toml
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd agentic-ai
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 LLM Setup (Ollama)

1. Install Ollama: https://ollama.com
2. Pull model:

```bash
ollama pull llama3
```

3. Ensure Ollama is running:

```
http://localhost:11434
```

---

## 📚 RAG Setup

### Step 1: Add Documents

Edit:

```
data/docs.txt
```

---

### Step 2: Run Ingestion

```bash
python rag/ingest.py
```

This will:

* create embeddings
* store them in ChromaDB (`chroma_db/`)

---

### Step 3: Run Application

```bash
python app.py
```

---

## ▶️ Example Usage

```
You: What is CAP theorem?
Agent: A distributed system can provide only two of consistency, availability...
```

---

## 🔁 How It Works

```
User Query
   ↓
Agent
   ↓
Retrieval Tool (RAG)
   ↓
LLM (with injected context)
   ↓
Response
```

### Flow Explanation

* The agent retrieves relevant context from a vector database
* Context is injected into the LLM prompt
* The LLM generates a grounded response

⚠️ Currently:

* Retrieval is always triggered (no decision logic yet)

---

## 🧩 Design Principles

* **Separation of concerns**
* **Interface-first design**
* **Incremental capability building**
* **Extensibility over shortcuts**

---

## 🧠 Architectural Intent

| Component | Responsibility                    |
| --------- | --------------------------------- |
| Agent     | Orchestration and control         |
| Tool      | External capabilities (RAG, APIs) |
| LLM       | Text generation                   |
| RAG       | Knowledge retrieval               |
| Models    | Structured communication          |

---

## ⚠️ Current Limitations

* Retrieval is always invoked (no conditional logic yet)
* No ranking/re-ranking of results
* No context compression
* No hallucination validation
* No citations in responses

---

## 🚀 Roadmap

### Step 3

* Decision-making agent (conditional retrieval)

### Step 4

* Tool selection and orchestration

### Step 5

* Validation and hallucination control

### Step 6+

* Memory, observability, scaling

---

## 🧠 Architecture Evolution

| Stage   | Capability            |
| ------- | --------------------- |
| Step 0  | System skeleton       |
| Step 1  | LLM integration       |
| Step 2  | RAG with persistence  |
| Step 3  | Conditional reasoning |
| Step 4+ | Enterprise hardening  |

---

## 📓 Development Approach

Each step follows:

* Goal
* Architecture delta
* Minimal implementation
* Test scenario
* Reflection

---

## 🧠 Learning Objective

This project is designed to build:

* Deep understanding of **agent systems**
* Ability to design **non-deterministic architectures**
* Enterprise mindset for **AI system reliability and control**

---

## ⚠️ Notes

* Built **from scratch (no frameworks initially)**
* Focus on **first principles and architecture**
* Framework comparison will be added later

---

## 📌 Next Step

Proceed to:

👉 **Step 3 — Decision-Making Agent (Conditional Retrieval)**

---

## 👨‍💻 Author

Built as part of a structured exploration into **Agentic AI systems and enterprise-grade design thinking**.

---
