#!/usr/bin/env python3
"""
Test script to verify Gemini API key is working
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('backend/.env')

def test_gemini_api():
    """Test the Gemini API key"""
    api_key = os.getenv('GEMINI_API_KEY')
    
    print(f"🔑 API Key: {api_key[:10]}...{api_key[-10:] if api_key else 'None'}")
    
    if not api_key:
        print("❌ No API key found!")
        return False
    
    try:
        # Clear any existing Google Cloud credentials that might interfere
        if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
            del os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        
        # Configure Gemini with just the API key
        genai.configure(api_key=api_key)
        
        # Test with a simple model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, can you respond with 'API is working'?")
        
        print(f"\n✅ API Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        
        # Try with a different model
        try:
            print("🔄 Trying with gemini-pro...")
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("Hello, can you respond with 'API is working'?")
            print(f"✅ API Response: {response.text}")
            return True
        except Exception as e2:
            print(f"❌ Second attempt failed: {str(e2)}")
            return False

if __name__ == "__main__":
    print("🧪 Testing Gemini API Key...")
    print("=" * 50)
    
    success = test_gemini_api()
    
    if success:
        print("\n🎉 Gemini API is working correctly!")
    else:
        print("\n⚠️ Gemini API test failed. Check your API key.")