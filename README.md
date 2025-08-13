# 📊 University Program Marketing Content Generator

The **University Program Marketing Content Generator** is a modular, Python-based application that automates the process of building and evaluating marketing content for university degree programs — specifically Master's programs in Data Science. It scrapes university program pages, intelligently filters the most relevant content, summarizes it into clean Markdown brochures using Large Language Models (LLMs), and then compares those brochures from the perspective of a prospective student.

Whether you're a researcher, prospective applicant, or marketing analyst, this tool provides an end-to-end pipeline for collecting, synthesizing, and comparing academic programs using modern AI methods.

---

## 🔧 How It Works

1. **Scraping**  
   The tool uses `BeautifulSoup` and `requests` to scrape a university program's landing page and extract all links and clean text from the HTML body.

2. **LLM-Based Link Filtering**  
   The scraped links are passed to an LLM (OpenAI or Ollama) to identify only those relevant to marketing purposes — like curriculum, about, admissions, and program structure pages. It excludes privacy, legal, and contact pages.

3. **Content Aggregation**  
   After selecting relevant links, the system revisits each of those URLs, scrapes the content, and stitches it into a single aggregated source of truth.

4. **Brochure Generation**  
   An LLM is prompted to summarize the cleaned, multi-page content into a polished, professional Markdown brochure for the program — including academic highlights, career outcomes, diversity metrics, and admissions info.

5. **Program Evaluation**  
   You can generate brochures for multiple schools, then use an LLM to **rank** them in order of how appealing or effective the program seems to a prospective student.

---

## ✨ Features

- **Modular LLM Integration**: Choose between OpenAI (`gpt-4o-mini`), local Ollama (`llama3.2`), or Ollama via OpenAI’s Python client interface.
- **Prompt Engineering**: Structured system/user prompts ensure consistency across scraping, selection, generation, and evaluation stages.
- **Multi-University Comparison**: Easily expand beyond UW, UT Austin, and UChicago to any academic program website.
- **Markdown Output**: Brochures are formatted for display on websites, documentation systems, or email campaigns.
- **CLI Workflow**: Run via command line with input prompts — perfect for batch comparisons or testing new models.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/university-program-marketing-generator.git
cd university-program-marketing-generator
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key
```bash
OPENAI_API_KEY=sk-your-api-key-here
```

## Project Structure
```pgsql
marketing_generator/
├── config.py              # Environment loading, constants
├── scraping.py            # Webpage scraping and text cleaning
├── prompts.py             # LLM system/user prompt templates
├── aggregator.py          # Gathers full content from relevant links
├── brochure.py            # LLM-driven brochure generation
├── evaluate.py            # Ranks brochures using an LLM
├── link_selector.py       # Filters links using JSON response
│
├── llm_clients/
│   ├── openai_client.py   # OpenAI API wrapper
│   ├── ollama_client.py   # Native Ollama wrapper
│   └── ovo_client.py      # Ollama via OpenAI interface
│
scripts/
├── run_brochures.py       # CLI tool to generate brochures
└── rank_programs.py       # CLI tool to compare/rank brochures
```

## ▶️ Usage Guide

To generate brochures, run the following:

```bash
python -m scripts.run_brochures
```
You’ll be prompted to choose an LLM backend:
```md
A: OpenAI (GPT)
B: Ollama (Llama 3.2)
C: Ollama via OpenAI interface
```
You can respond with the letter options or with the client names. upper/lower case are both acceptable.

The script will scrape and summarize three university programs:
```md
University of Washington
University of Texas (Online)
University of Chicago
```
Each program is turned into a polished marketing-style brochure formatted in Markdown.
To rank the brochures, run the evaluator:
```bash
python -m scripts.rank_programs
```
This will:
Load the generated brochures
Prompts the LLM to act as a prospective Data Science student
Ranks the three programs and explains the reasoning

## ⚙️ Requirements
- Python 3.9+
- An OpenAI account or a local Ollama server
- Internet access to fetch university web pages
- (Optional) Ollama installed with the llama3 model

## 🧩 Extending the Project
This codebase is built to be modular and extensible. You can:
- Add new schools by editing the URL list in scripts/run_brochures.py
- Swap in new models by editing the logic in llm_clients/
- Replace the Markdown output with PDF or HTML export options
- Enhance the ranking system with custom weights (e.g., cost, job placement, city)

## 👨‍💻 Author
Built by [Marcus Curry](https://www.linkedin.com/in/currymarcus/) — Data Scientist, Engineer, and LLM Systems Builder.


