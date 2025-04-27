import os
import requests

# Get API Key from environment variable
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    print("❌ ERROR: API key not found! Set it using export NEWS_API_KEY='your_api_key'")
    exit()

# Use 'everything' endpoint to fetch all news
url = f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&language=en&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

# Debugging: Print API Response
print(f"🔍 API Response Code: {response.status_code}")
print(f"🔍 API Response JSON: {data}")

if data.get("status") != "ok":
    print(f"❌ API Error: {data.get('message')}")
    exit()

articles = data.get("articles", [])

if not articles:
    print("❌ No articles found in API response!")
    exit()

# Save news articles to a file
with open("all_news.txt", "w") as file:
    for article in articles:
        file.write(f"{article['title']} - {article['source']['name']}\n")
        file.write(f"{article['description']}\n")
        file.write(f"🔗 {article['url']}\n\n")

print("✅ All news articles saved to all_news.txt")

