# MeetStream Transcript Summarizer (CLI)

A CLI tool that ingests a meeting transcript (.txt) and generates a clear, actionable bullet-point summary using a large language model.


## Features
* **Reads meeting transcripts from a text file** 
* **Generates executive-style bullet point summaries**
* **Uses LangChain with LCEL for clean chaining**
* **Spinner-based CLI feedback for better UX**
* **Strong error handling for missing files, empty input, and API keys**

## Model & API Choice
This project uses an OpenAI-compatible model via the Groq API.

**Why Groq?**

* I do not currently have an active OpenAI API subscription

* Groq provides OpenAI-compatible chat models with very low latency

* The code is structured so switching to ChatOpenAI only requires changing the LLM initialization


## Tech Stack

* Python 3.11
* LangChain (LCEL)
* Groq API
* argparse (CLI parsing)
* dotenv (environment variables)
* threading (spinner UX)

## Installation 

1.  **Clone & Install**
    ```bash
    git clone [https://github.com/SKrishna-07/meetstream-summarizer.git](https://github.com/YourUsername/meetstream-summarizer.git)
    cd meetstream-summarizer
    pip install -r requirements.txt
    ```

2.  **Configure Environment**
    * Get a free API key from [Groq Console](https://console.groq.com/).
    * Export it in your terminal:
    ```bash
    export GROQ_API_KEY='gsk_your_key_here'
    ```

3.  **Run the Summarizer**
    ```bash
    python main.py transcript.txt
    ```

## 📂 Example Output
```text
⚡ Ingesting transcript via Groq LPU (Llama 3.3 70B)...

════════════════════════════════════════
 📝 INTELLIGENT SUMMARY
════════════════════════════════════════

**Decisions:**
* Rate Limiter implementation will use Redis.
* Release scheduled for Friday morning.

**Action Items:**
* [Sam] Fix midnight counter reset bug by tonight.
* [Sam] Update Swagger documentation immediately.
* [Jordan] Finalize UI integration by tomorrow.

**Blockers:**
* Frontend team is currently blocked by outdated API docs.