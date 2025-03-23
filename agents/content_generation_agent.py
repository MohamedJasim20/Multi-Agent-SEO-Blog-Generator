from models.llm_model import generate_text

class ContentGenerationAgent:
    def generate_content(self, outline):
        print("Generating content from outline...")
        prompt = f"""
        Write a detailed, engaging blog post based on this outline:
        {outline}
        """
        content = generate_text(prompt)
        print("Content generation complete.")
        return content
