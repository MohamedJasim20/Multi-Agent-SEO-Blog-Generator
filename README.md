# Multi-Agent SEO Blog Generator

## Overview
The **Multi-Agent SEO Blog Generator** is a Python-based system that uses multiple agents to research trending topics, gather information, and generate SEO-optimized blog posts using **LLMs (Large Language Models)**. It automates content creation by integrating **SerpAPI**, **LangChain**, and **Hugging Face Transformers**.

---

## 🏗️ System Architecture

The project follows a **multi-agent system** architecture, where each agent has a specific responsibility:

1. **Research Agent**  
   - Fetches trending topics from Google using **SerpAPI**  
   - Gathers relevant information from multiple sources  

2. **Content Generation Agent**  
   - Uses a **pre-trained LLM (Flan-T5, GPT-3, or LLaMA)**  
   - Generates structured and SEO-friendly blog posts  

3. **File Management Agent**  
   - Saves the generated blog post in Markdown (`.md`), HTML, and PDF formats  
   - Uploads content to a destination (GitHub/Google Drive)  

---

## 🔄 Agent Workflow

1️⃣ **Fetch Trending Topics**  
   - Uses SerpAPI to extract popular search queries.  
   - Example: "Top AI trends in 2025"  

2️⃣ **Gather Information**  
   - Uses web scraping APIs or pre-collected datasets.  

3️⃣ **Generate Blog Content**  
   - Uses an **LLM** (Flan-T5, GPT-3, or OpenAI API).  

4️⃣ **Save Output Files**  
   - Markdown (`.md`), HTML, and PDF are generated automatically.  

---

## 🛠️ Tools & Frameworks Used

| Component  | Technology Used |
|------------|----------------|
| Programming Language | Python |
| API Integration | SerpAPI |
| Language Model | Hugging Face (Flan-T5) |
| Framework | LangChain |
| Output Formats | Markdown, HTML, PDF |

---

## 🚀 Installation & Execution

### 1️⃣ Install Dependencies  
```bash
git clone https://github.com/MohamedJasim20/Multi-Agent-SEO-Blog-Generator.git
cd Multi-Agent-SEO-Blog-Generator
pip install -r requirements.txt
