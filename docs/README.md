# Customer Feedback Sys

## Overview
This is an AI-powered platform designed to:
    1. Collect customer feedback
    2. Classify the feedback into 3 categories (Compliment/positive, Complaint/Negative and          Neutral) This uses NLP
    3. Detect/extract problems from the feedback received
    4. Use AI(RAG & LLM) to suggest solutions
    5. Embedding storage for similarity search
    6. Visualize categories in a dashboard (Dash + plotly)
    7. Provide a chat interface for user interaction

## Architecture
User >> Chat UI >>FastAPI >>NLP Pipeline >> DB


        User → Chat UI → FastAPI → NLP Pipeline → DB
        ↓
        Embeddings
        ↓
        RAG Retrieval
        ↓
        LLM
        ↓
        Response

Dashboard reads from DB then visualizes insights


Backend API >> FastAPI
Dashboard   >> Dash + Plotly
Database    >> SQLite 
NLP         >> Transformers
Embeddings  >> SentenceTransformers 
LLM         >> LLaMA3
Deployment  >> ____________Docker to e configured

## How to run
    ### Local
    ```bash
    uvicorn app.main:app --reload
    python dash_app.py
    python chat_app.py

    ### Docker
    docker compose up --build

## Services 
    API          http://127.0.0.1:8000
    Dashboard    http://127.0.0.1:8050
    Chat UI      http://127.0.0.1:8051

## Pipeline
1. user sumbits feedback
2. Text is classified
3. Problem is extracted
4. Embedding  generated
5. Similar past problems retrieved (RAG)
6. LLM generates solution
7. Stored in database

## Database Schema
id                  Integer
text                string
category            string
problem             string
suggestion          string
rule_suggestion     string
llm_analysis        text
final_solution      text
embedding           BLOB
created_at          timestamp


## Dashboard
Feedback category distribution   >> pie chart
Problem topic distribution       >> pie chart
Feedback over time               >> histogram
Feedback table

## Chat UI
send feedback
receive response in form of a solution
both feedback and response stored in DB

