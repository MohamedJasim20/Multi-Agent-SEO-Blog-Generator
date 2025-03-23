from serpapi import GoogleSearch
import json

class ResearchAgent:
    def __init__(self, serpapi_key):
        self.serpapi_key = serpapi_key

    def fetch_trending_topics(self):
        print("Fetching trending HR topics...")

        params = {
            "q": "trending HR topics 2024",
            "api_key": self.serpapi_key,
            "engine": "google",
            "num": 5
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()  # Correct method to dict JSON response
            print(f"Raw SerpAPI Response: {json.dumps(results, indent=2)}")  # Debugging

            # Extract trending topics
            topics = [result['title'] for result in results.dict("organic_results", [])]
            if not topics:
                raise ValueError("No trending topics found.")

            print(f"Trending topics found: {topics}")
            return topics

        except Exception as e:
            print(f"Error fetching trending topics: {e}")
            return ["Fallback Topic: AI in HR"]


    def gather_information(self, topic):
        print(f"Gathering research data for topic: {topic}")
        params = {
            "q": topic,
            "api_key": self.serpapi_key,
            "engine": "google",
            "num": 10
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        snippets = [result.get('snippet', '') for result in results.get("organic_results", [])]
        print(f"Collected {len(snippets)} snippets of information.")
        return " ".join(snippets)
