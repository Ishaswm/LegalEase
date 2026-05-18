#!/bin/bash

# Deploy Legal EASE after local testing
echo "🚀 Deploying Legal EASE to Google Cloud Run..."

gcloud run deploy lexi-simplify \
  --source . \
  --region us-central1 \
  --set-env-vars "GEMINI_API_KEY,GOOGLE_CLOUD_PROJECT,VERTEX_AI_LOCATION,FLASK_ENV=production,MAX_FILE_SIZE=10485760,SESSION_TIMEOUT=3600" \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 1 \
  --timeout 300 \
  --concurrency 10 \
  --max-instances 10

echo "✅ Deployment complete!"
echo "🌐 Your Legal EASE app: https://lexi-simplify-822987556610.us-central1.run.app"
