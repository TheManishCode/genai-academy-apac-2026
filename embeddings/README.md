# Embeddings

Recommended production index:

- Store source documents in Cloud Storage.
- Chunk disaster SOPs, citizen report summaries, ward profiles and hospital readiness notes.
- Generate embeddings using Vertex AI text embedding models.
- Store vectors in AlloyDB, BigQuery vector search or Vertex AI Vector Search.
- Retrieve top-k context for Gemini before generating recommendations.
