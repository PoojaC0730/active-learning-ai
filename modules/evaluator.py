from modules.groq_client import call_llm
import logging

logger = logging.getLogger(__name__)

def evaluate_short_answer(question, correct_answer, user_answer):
    logger.info("Evaluating short answer...")
    prompt = f"""
    Evaluate the student's short answer semantically.
    Does the user's answer capture the core idea of the concept? 
    Do not enforce exact matching, focus on meaning and understanding.

    Question: {question}
    Reference Correct Answer: {correct_answer}
    Student's Answer: {user_answer}

    Return strict JSON format:
    {{
      "score": <int 0-5>,
      "correctness": <boolean true or false (true if score >= 3)>,
      "reasoning": "<string: brief explanation of your evaluation>"
    }}
    """

    result = call_llm(prompt, temperature=0)
    if result is None:
        logger.error("Failed to generate evaluation from LLM.")
    return result
