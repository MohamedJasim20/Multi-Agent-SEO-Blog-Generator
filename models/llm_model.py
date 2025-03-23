from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load open-source LLM model
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-1.3b")
model = AutoModelForCausalLM.from_pretrained("facebook/opt-1.3b")

def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=1024)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
