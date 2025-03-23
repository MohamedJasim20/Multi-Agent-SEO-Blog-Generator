from models.llm_model import generate_text

class ContentPlanningAgent:
    def generate_outline(self, topic, research_data):
        print(f"Generating outline for topic: {topic}")
        prompt = f"""
        Generate a structured outline for a 2000-word blog on '{topic}'. 
        Use the following research:
        {research_data}
        """
        outline = generate_text(prompt)
        print("Outline generated.")
        return outline
