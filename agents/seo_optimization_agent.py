import re

class SEOOptimizationAgent:
    def optimize_content(self, content):
        print("Optimizing content for SEO...")
        keywords = ["HR trends", "human resources", "employee engagement", "workplace"]
        for keyword in keywords:
            content = re.sub(r'\b' + re.escape(keyword.split()[0]) + r'\b', keyword, content, count=5)
        print("SEO optimization completed.")
        return content
