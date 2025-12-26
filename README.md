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


## Error Handling

* The tool gracefully handles:
* Missing or invalid file paths
* Empty transcript files
* Missing API keys
* Dependency issues

## Switching to OpenAI API (Optional)

1. To use OpenAI directly:
2. Replace ChatGroq with ChatOpenAI
3. Set OPENAI_API_KEY in .env
3. Uncomment the OpenAI-related code

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
    git clone [https://github.com/SKrishna-7/meetstream-summarizer.git](https://github.com/SKrishna-7/meetstream-summarizer.git)
    cd meetstream-summarizer
    pip install -r requirements.txt
    ```

2.  **Configure Environment**
    * Get a free API key from [Groq Console](https://console.groq.com/home).
    * Create a .env file in the project root:
    ```bash
     GROQ_API_KEY='gsk_your_key_here'
    ```

3.  **Run the Summarizer**
    ```bash
    python summarizer.py transcript.txt
    ```

## Example input 
```
Speaker 1 (Alex): Alright, let's get started. Thanks for joining, everyone. The main goal for today is to finalize the launch plan for the new API Rate Limiting feature. Sam, can you give us an update on the backend?

Speaker 2 (Sam): Yeah, sure. So, the Redis implementation is basically done. I've tested it with about 10,000 concurrent requests, and latency looks good. It's holding up under 50ms. However, I did run into a small edge case where the counter doesn't reset correctly if the server restarts exactly at midnight UTC. I need maybe half a day to patch that.

Speaker 1 (Alex): Okay, that sounds manageable. Do you think you can deploy the fix to staging by tomorrow morning?

Speaker 2 (Sam): Yes, definitely. I'll push the fix tonight.

Speaker 3 (Jordan): From the frontend side, the dashboard UI is ready, but I'm currently blocked. I need the updated API documentation to know exactly what error codes the rate limiter returns. Is it returning a 429 status code with a standard JSON body?

Speaker 2 (Sam): Ah, right. I forgot to update the Swagger docs. Yes, it returns a 429. I'll update the documentation immediately after this call so you're unblocked.

Speaker 1 (Alex): Great. So, Jordan, once you have the docs, how long until we can merge the UI?

Speaker 3 (Jordan): If I get the docs today, I can finish the integration tomorrow and we can do a full end-to-end test on Thursday.

Speaker 1 (Alex): Perfect. Let's aim for that. So, to recap: Sam is fixing the midnight bug and updating docs today. Jordan finishes UI integration tomorrow. We aim for a code freeze on Thursday and release on Friday morning. Does that work for everyone?

Speaker 2 (Sam): Works for me.

Speaker 3 (Jordan): Sounds good.

Speaker 1 (Alex): Awesome. Thanks, everyone. Let's break.

```


## 📂 Example Output

**════════════════════════════════════════**
  ##  MEETING SUMMARY
**════════════════════════════════════════**

**Meeting Summary – API Rate Limiting Feature Launch**

- **Backend (Redis implementation)**
  - **Issue:** Counter reset fails if server restarts exactly at midnight UTC.
  - **Action:** Patch the edge‑case bug.
  - **Owner:** Sam
  - **Deadline:** Patch to be completed and pushed to **staging tonight**; fix deployed to staging by **tomorrow morning**.

- **API Documentation**
  - **Missing:** Updated Swagger docs showing error response.
  - **Action:** Add 429 status code with standard JSON body to docs.
  - **Owner:** Sam
  - **Deadline:** Immediately after the call (today) so the frontend team can proceed.

- **Frontend (Dashboard UI)**
  - **Current status:** UI ready but blocked awaiting updated docs.
  - **Action:** Integrate rate‑limiter error handling once docs are received.
  - **Owner:** Jordan
  - **Deadline:** Complete integration **tomorrow**; ready for end‑to‑end testing **Thursday**.

- **Testing & Release Timeline**
  - **Thursday:** Full end‑to‑end test and code freeze.
  - **Friday morning:** Production release of the API Rate Limiting feature.

- **Next Steps / Follow‑ups**
  - Sam → push bug fix to staging tonight & update Swagger docs today.
  - Jordan → finish UI integration tomorrow after receiving docs.
  - All → verify end‑to‑end flow on Thursday; prepare release notes for Friday launch.
