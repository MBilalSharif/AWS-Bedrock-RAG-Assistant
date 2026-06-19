# Amazon Bedrock RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using **Amazon Bedrock Knowledge Bases** and the **RetrieveAndGenerate API**. The chatbot answers questions using documents stored in Amazon S3 instead of relying solely on the foundation model's knowledge.

As an enhancement, AWS Lambda is used during ingestion to automatically extract metadata from documents, improving retrieval quality and enabling metadata-aware searches.

---

## Features

* Amazon Bedrock Knowledge Base
* Amazon S3 document storage
* Python chatbot
* RetrieveAndGenerate API
* AWS Lambda metadata extraction
* Automatic document ingestion
* Semantic search with vector embeddings
* Comparison between Direct LLM and RAG responses
* Retrieval accuracy evaluation

---

## Architecture

```
Documents (PDFs)
        │
        ▼
Amazon S3 Bucket
        │
        ▼
AWS Lambda
(Metadata Extraction)
        │
        ▼
Amazon Bedrock Knowledge Base
(Vector Embeddings + Index)
        │
        ▼
RetrieveAndGenerate API
        │
        ▼
Python Chatbot
        │
        ▼
Grounded Response
```

---

## Project Structure

```
.
├── chatbot.py                 # Python chatbot
├── metadata_extractor.py  # Lambda function
└── README.md
```

---

## Technologies Used

* Python
* Amazon Bedrock
* Amazon Bedrock Knowledge Bases
* Amazon S3
* AWS Lambda
* Boto3

---

## Knowledge Base

The knowledge base contains domain-specific AWS documentation stored in Amazon S3. During ingestion:

* Documents are chunked
* Vector embeddings are generated
* Metadata is extracted using AWS Lambda
* Chunks are indexed for semantic retrieval

---

## Evaluation

The chatbot was evaluated using:

* **10 total questions**

  * 5 answerable from the knowledge base
  * 5 intentionally outside the available documents

The evaluation included:

* Retrieval accuracy
* Chunk relevance
* Direct LLM vs RAG comparison
* Hallucination reduction
* Effectiveness of the chosen chunking strategy

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<username>/bedrock-rag-chatbot.git
cd bedrock-rag-chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure AWS Credentials

Configure your AWS credentials using the AWS CLI or environment variables.

### Run

```bash
python chatbot.py
```

---

## Learning Outcomes

This project demonstrates:

* Building Retrieval-Augmented Generation applications
* Working with Amazon Bedrock Knowledge Bases
* Using the RetrieveAndGenerate API
* Metadata enrichment with AWS Lambda
* Evaluating retrieval quality
* Reducing hallucinations using grounded responses

---

## License

This project is intended for educational and learning purposes.
