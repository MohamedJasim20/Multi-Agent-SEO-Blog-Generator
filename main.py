from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_optimization_agent import SEOOptimizationAgent
from agents.review_agent import ReviewAgent

import os

# Load SerpAPI Key from Environment Variables or Hardcode (Not Recommended)
serpapi_key = os.getenv("SERPAPI_KEY", "87f88f066c12fe750ede01cc594943c693790cc8f5255d6e1291c33d5ce7a61e")  # Replace if needed

def save_blog_as_md(content, filename="blog_post.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"# Generated HR Blog\n\n{content}\n")
    print(f"✅ Blog post saved as {filename}")

def generate_blog(serpapi_key):
    print("\n🔹 Starting blog generation process...")

    # Initialize agents
    research_agent = ResearchAgent(serpapi_key)
    planning_agent = ContentPlanningAgent()
    generation_agent = ContentGenerationAgent()
    seo_agent = SEOOptimizationAgent()
    review_agent = ReviewAgent()

    # 1️⃣ Fetch Trending Topics
    print("\n📌 Fetching trending HR topics...")
    trending_topics = research_agent.fetch_trending_topics()
    
    if not trending_topics or trending_topics == ["Fallback Topic: AI in HR"]:
        print("⚠️ No trending topics found! Check API key or internet connection.")
        return

    selected_topic = trending_topics[0]
    print(f"✅ Selected Topic: {selected_topic}")

    # 2️⃣ Gather Research Data
    print("\n📌 Gathering information for the topic...")
    research_data = research_agent.gather_information(selected_topic)

    if not research_data.strip():
        print("⚠️ No research data found! Using fallback data.")
        research_data = "AI in HR is changing workforce management significantly."

    print("\n📌 Research Data Collected!")

    # 3️⃣ Generate Blog Outline
    print("\n📌 Generating Blog Outline...")
    outline = planning_agent.generate_outline(selected_topic, research_data)
    print("✅ Outline Generated!\n")

    # 4️⃣ Generate Blog Content
    print("\n📌 Generating Blog Content...")
    raw_content = generation_agent.generate_content(outline)
    print("✅ Content Generation Complete!\n")

    # 5️⃣ Optimize for SEO
    print("\n📌 Optimizing Content for SEO...")
    seo_content = seo_agent.optimize_content(raw_content)
    print("✅ SEO Optimization Done!\n")

    # 6️⃣ Proofread & Finalize
    print("\n📌 Proofreading & Finalizing Content...")
    final_content = review_agent.proofread(seo_content)
    print("✅ Proofreading Complete!\n")

    print("\n🎉 Blog generation process completed!")
    return final_content

if __name__ == "__main__":
    blog_post = generate_blog(serpapi_key)  # Pass the SerpAPI key as an argument
    print(f"SerpAPI Key: {serpapi_key}")
    if blog_post:
        print("\n📝 **Generated Blog Post:**\n")
        print(blog_post)
    else:
        print("\n⚠️ Blog generation failed. Please check logs for issues.")
