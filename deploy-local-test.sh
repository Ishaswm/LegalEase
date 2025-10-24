#!/bin/bash

# Deploy Legal EASE after local testing
echo "🚀 Deploying Legal EASE to Google Cloud Run..."

gcloud run deploy lexi-simplify \
  --source . \
  --region us-central1 \
  --set-env-vars "GEMINI_API_KEY=AIzaSyDMwKAGpQ0tyly_cvk5uXxXCl87Ebnk6_Q,GOOGLE_CLOUD_PROJECT=causal-galaxy-415009,VERTEX_AI_LOCATION=us-central1,FLASK_ENV=production,MAX_FILE_SIZE=10485760,SESSION_TIMEOUT=3600" \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 1 \
  --timeout 300 \
  --concurrency 10 \
  --max-instances 10

echo "✅ Deployment complete!"
echo "🌐 Your Legal EASE app: https://lexi-simplify-822987556610.us-central1.run.app"