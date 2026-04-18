from modules.groq_client import call_llm
import logging
import json

logger = logging.getLogger(__name__)

def generate_quiz(text):
    logger.info("Generating standard quiz...")
    prompt = f"""
    You are an expert educator.

    Generate multiple choice questions based on Bloom's taxonomy.
    Create exactly 3 questions for each of the following difficulty levels:
    - Easy: Direct factual recall
    - Medium: Conceptual understanding
    - Hard: Application / reasoning

    For each question, provide a helpful hint that does not reveal the answer directly.

    Content:
    {text}

    Output STRICT JSON:
    {{
      "easy": [
        {{
          "concept": "",
          "question": "",
          "options": ["", "", "", ""],
          "answer": "",
          "hint": ""
        }}
      ],
      "medium": [
        {{
          "concept": "",
          "question": "",
          "options": ["", "", "", ""],
          "answer": "",
          "hint": ""
        }}
      ],
      "hard": [
        {{
          "concept": "",
          "question": "",
          "options": ["", "", "", ""],
          "answer": "",
          "hint": ""
        }}
      ]
    }}
    """

    result = call_llm(prompt)
    if result is None:
        logger.error("LLM failed to generate standard quiz.")
    return result

def generate_fusion_quiz(chunks):
    logger.info("Generating fusion quiz...")
    prompt = f"""
    You are an expert educator.

    You are given multiple pieces of content from different sources.

    Your task:
    1. Combine the knowledge
    2. Remove redundancy
    3. Identify key concepts
    4. Generate 3 multiple choice questions for each difficulty level based on Bloom's taxonomy:
       - Easy: Direct factual recall
       - Medium: Conceptual understanding
       - Hard: Application / reasoning

    For each question, provide a helpful hint that does not reveal the answer directly.

    Content:
    {chunks}

    Output STRICT JSON:
    {{
      "concepts": ["", ""],
      "easy": [
        {{
          "concept": "",
          "question": "",
          "options": ["", "", "", ""],
          "answer": "",
          "hint": ""
        }}
      ],
      "medium": [
        {{
          "concept": "",
          "question": "",
          "options": ["", "", "", ""],
          "answer": "",
          "hint": ""
        }}
      ],
      "hard": [
        {{
          "concept": "",
          "question": "",
          "options": ["", "", "", ""],
          "answer": "",
          "hint": ""
        }}
      ]
    }}
    """

    result = call_llm(prompt)
    if result is None:
        logger.error("LLM failed to generate fusion quiz.")
    return result

def generate_explanation(question, user_choice, correct_choice, concept):
    logger.info("Generating explanation for wrong answer...")
    prompt = f"""
    A student answered a multiple choice question incorrectly. 
    Explain why the correct answer is right, why their choice is wrong, and briefly review the core concept they missed.

    Question: {question}
    Student's Choice: {user_choice}
    Correct Answer: {correct_choice}
    Related Concept: {concept}

    Provide a brief, encouraging paragraph (max 3 sentences).
    """
    result = call_llm(prompt, temperature=0.3)
    if result is None:
        logger.error("LLM failed to generate explanation.")
        return "Explanation could not be generated at this time."
    return result

def generate_redemption_questions(weak_concepts):
    logger.info("Generating redemption questions...")
    concepts_str = ", ".join(weak_concepts)
    prompt = f"""
    The student struggled with the following concepts during the quiz:
    {concepts_str}

    Generate 1 or 2 SHORT ANSWER questions to test their semantic understanding of these concepts.
    Do NOT provide options. The student will type their answer.

    Output STRICT JSON format exactly like this:
    {{
      "questions": [
        {{
          "concept": "",
          "question": "",
          "correct_answer": "Brief reference answer for evaluation context"
        }}
      ]
    }}
    """
    result = call_llm(prompt, temperature=0.7)
    if result is None:
        logger.error("LLM failed to generate redemption questions.")
    return result
