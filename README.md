# Active Learning AI

An adaptive, personalized learning platform built using Python and Streamlit. The application leverages Large Language Models (LLMs) to automatically generate educational assessments tailored to different levels of cognitive difficulty based on Bloom's Taxonomy. It transforms passive reading material into a highly interactive, measurable learning cycle.

## Features

- **Dynamic Quiz Generation:** Enter plain text or upload a collection of topic PDFs to automatically extract core concepts and generate a structured quiz.
- **Cognitive Level Scaling:** Evaluates understanding across three tiers: Easy (Factual Recall), Medium (Conceptual Understanding), and Hard (Application/Reasoning).
- **Concept Level Graph & Tracking:** Automatically maps every generated question to a specific conceptual topic and calculates mastery metrics in real-time.
- **Explainability Layer:** Acts as an instant AI tutor. Incorrect answers are met with an automatically generated explanation of why the selected option was wrong, why the reference choice was correct, and a review of the missed concept.
- **Iterative Learning Loop (Redemption Round):** The system tracks concepts the user stumbled on. Upon finishing the main quiz, it generates a personalized "Redemption Round" to test the remaining knowledge gaps.
- **Semantic Evaluation:** The Redemption Round uses short-answer text fields. The AI evaluates the submitted answers semantically (out of 5 points) to ensure the core idea is understood, completely replacing naive exact-match keyword comparison.
- **Analytics Dashboard:** A sidebar dashboard provides a visual breakdown of cumulative accuracy and per-concept mastery via interactive bar charts.

## Prerequisites

- Python 3.9 or higher
- An active Groq API Key (or an equivalent LLM provider key if you choose to swap the backend)

## Installation

1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your environment variables. Create a `.env` file in the root directory and add your API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Start the Streamlit application by running:
```bash
streamlit run app.py
```

Navigate to the local URL provided in your terminal. You can test the engine by submitting a block of study text, or switch to the "Multi-Doc Fusion" tab to upload PDF documents. Follow the on-screen metrics and complete the quiz rounds to trigger the advanced evaluation capabilities. 

## Structure

- `app.py`: The entry point and main Streamlit user interface mapping out the learning loop architecture.
- `modules/quiz_generator.py`: Contains the LLM prompts designed for concept extraction, adaptive complexity generation, and dynamic explainability feedback generation.
- `modules/evaluator.py`: Features the semantic evaluator acting on short answers to judge whether concepts are fundamentally understood.
- `modules/text_processor.py`: Utilities for document parsing and data chunking.
- `utils/`: Miscellaneous parsing and formatting helpers.
