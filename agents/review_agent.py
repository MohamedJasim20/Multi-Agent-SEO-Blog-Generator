from transformers import pipeline

class ReviewAgent:
    def proofread(self, content):
        print("Proofreading content...")
        summarizer = pipeline("summarization")
        summary = summarizer(content, max_length=300, min_length=150, do_sample=False)
        print("Proofreading and summarization completed.")
        return summary[0]['summary_text'] if summary else content
