import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ No API key found in .env file")
    exit(1)

print(f"🔑 API Key found: {api_key[:10]}...{api_key[-4:]}")

try:
    # Initialize client
    client = genai.Client(api_key=api_key)
    
    # Test with a simple request
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Say 'Hello, API key is working!'"
    )
    
    result = response.candidates[0].content.parts[0].text
    print(f"✅ API Key is working! Response: {result}")
    
except Exception as e:
    print(f"❌ API Key error: {e}")
    print("\nPossible solutions:")
    print("1. Get a new API key from https://makersuite.google.com/app/apikey")
    print("2. Check if your .env file has the correct GEMINI_API_KEY=your_key_here")
    print("3. Make sure the API key is not expired") 