#!/usr/bin/env python3
"""
Test Gemini API using direct REST calls
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('backend/.env')

def test_rest_gemini():
    """Test Gemini API using REST calls"""
    api_key = os.getenv('GEMINI_API_KEY')
    
    print(f"🔑 API Key: {api_key[:10]}...{api_key[-10:] if api_key else 'None'}")
    
    if not api_key:
        print("❌ No API key found!")
        return False
    
    try:
        # First, list available models
        print("\n📋 Checking available models...")
        list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
        list_response = requests.get(list_url, timeout=30)
        
        if list_response.status_code == 200:
            models = list_response.json()
            print("Available models:")
            for model in models.get('models', []):
                if 'generateContent' in model.get('supportedGenerationMethods', []):
                    print(f"  - {model['name']}")
        
        # Try with a working model
        models_to_try = [
            "gemini-2.0-flash-exp",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro", 
            "gemini-pro"
        ]
        
        for model_name in models_to_try:
            print(f"\n🔄 Trying model: {model_name}")
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
            
            headers = {
                'Content-Type': 'application/json',
            }
            
            data = {
                "contents": [{
                    "parts": [{
                        "text": "Respond with exactly: 'REST API is working correctly'"
                    }]
                }]
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=30)
            
            print(f"📡 Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and len(result['candidates']) > 0:
                    text = result['candidates'][0]['content']['parts'][0]['text']
                    print(f"✅ API Response: {text}")
                    print(f"✅ Working model: {model_name}")
                    return True
                else:
                    print(f"❌ No candidates in response: {result}")
            else:
                print(f"❌ API Error: {response.status_code} - {response.text[:200]}...")
        
        return False
            
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Gemini REST API...")
    print("=" * 50)
    
    success = test_rest_gemini()
    
    if success:
        print("\n🎉 Gemini REST API is working!")
    else:
        print("\n⚠️ Gemini REST API test failed.")