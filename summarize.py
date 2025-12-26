import os
import sys
import time
import threading
import argparse
from dotenv import load_dotenv
load_dotenv()
# LangChain Imports
try:
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_groq.chat_models import ChatGroq

except ImportError:
    print("Error: Missing dependencies. Run 'pip install -r requirements.txt'")
    sys.exit(1)

# --- Spinner for UX ---
class Spinner:
    """A simple loading spinner for CLI feedback."""
    def __init__(self, message="Processing..."):
        self.message = message
        self.stop_running = False
        self.thread = threading.Thread(target=self._animate)

    def start(self):
        self.stop_running = False
        self.thread.start()

    def stop(self):
        self.stop_running = True
        self.thread.join()

    def _animate(self):
        chars = "/-\|"
        i = 0
        while not self.stop_running:
            sys.stdout.write(f"\r{self.message} {chars[i % 4]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")

# --- Core Logic ---
def read_file(file_path: str) -> str:
    """Reads and returns file content with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                raise ValueError("The file is empty.")
            return content
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")

def get_summary(text: str, model_name: str = "openai/gpt-oss-120b") -> str:
    """Generates a summary using LangChain LCEL."""
    
    # 1. Initialize Model
    # Expects OPENAI_API_KEY in env variables
    # llm = ChatOpenAI(model=model_name, temperature=0.3)
    
    llm = ChatGroq(model=model_name, temperature=0.3)

    # 2. Create Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an executive assistant. Summarize the provided meeting transcript into clear, actionable bullet points."),
        ("user", "{text}")
    ])

    # 3. Build Chain (Prompt -> LLM -> String Output)
    chain = prompt | llm | StrOutputParser()

    # 4. Invoke
    return chain.invoke({"text": text})

# --- CLI Entry Point ---
def main():
    parser = argparse.ArgumentParser(description="AI Meeting Summarizer CLI")
    parser.add_argument("file", help="Path to the transcript text file")
    parser.add_argument("--save", action="store_true", help="Save the summary to a .txt file")
    args = parser.parse_args()

    # check API key
    # if not os.environ.get("OPENAI_API_KEY"):
    #     print("Error: OPENAI_API_KEY environment variable is not set.")
    #     print("   Run: export OPENAI_API_KEY='sk-...'")
    #     sys.exit(1)
    
    if not os.environ.get("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY environment variable is not set.")
        sys.exit(1)
    

    try:
        # Step 1: Read
        transcript = read_file(args.file)
        
        # Step 2: Summarize (with spinner)
        spinner = Spinner("✨ Analyzing transcript...")
        spinner.start()
        try:
            summary = get_summary(transcript)
        finally:
            spinner.stop()

        # Step 3: Output
        print("\n" + "═" * 40)
        print("MEETING SUMMARY")
        print("═" * 40 + "\n")
        print(summary)
        print("\n" + "═" * 40)

        # Optional: Save to file
        if args.save:
            output_file = f"summary_{int(time.time())}.txt"
            with open(output_file, "w") as f:
                f.write(summary)
            print(f"\n✅ Summary saved to: {output_file}")

    except Exception as e:
        print(f"\n   Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()