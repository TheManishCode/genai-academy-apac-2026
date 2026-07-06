# Deployment Guide

## Google Cloud Setup

1. Create or select a Google Cloud project.
2. Enable Cloud Run, Artifact Registry, BigQuery, Cloud Storage, Vertex AI and Cloud Build.
3. Create a Firebase project and enable Google Authentication.
4. Create a BigQuery dataset named `ecomind`.
5. Create a Cloud Storage bucket for raw datasets and citizen media.

## Cloud Run Backend

```bash
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/ecomind-api -f docker/backend.Dockerfile .
gcloud run deploy ecomind-api \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/ecomind-api \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT,BIGQUERY_DATASET=ecomind
```

## Cloud Run Frontend

```bash
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/ecomind-web -f docker/frontend.Dockerfile .
gcloud run deploy ecomind-web \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/ecomind-web \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars VITE_API_BASE_URL=https://YOUR_API_URL/api/v1
```

## NVIDIA RAPIDS

For GPU training or inference, use a GPU-enabled runtime image such as an NVIDIA CUDA base image and install RAPIDS packages from the official RAPIDS channel. Keep the API image slim and run GPU jobs as scheduled Cloud Run jobs, Vertex AI custom training jobs, or GKE workloads with NVIDIA GPUs.
