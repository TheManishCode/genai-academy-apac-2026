# RAG Pipeline

The backend includes `backend/app/rag/pipeline.py`, which demonstrates how EcoMind grounds Gemini responses.

Production sources:

- BigQuery ward-level risk forecasts
- Cloud Storage citizen media summaries
- OpenAQ and weather station snapshots
- Hospital and emergency resource tables
- Disaster playbooks and city SOPs

Answer format:

1. Direct answer
2. Confidence
3. Why the risk exists
4. Recommended actions
5. Generated SQL
6. Citations
