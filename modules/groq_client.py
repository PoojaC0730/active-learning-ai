from groq import Groq
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt, temperature=0.7):
    try:
        logger.info("Sending request to LLM...")
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        logger.info("Successfully received LLM response.")
        raw_content = response.choices[0].message.content
        logger.info(f"Raw LLM response:\n{raw_content}")
        return raw_content
    except Exception as e:
        logger.error(f"LLM API call failed: {e}")
        return None
