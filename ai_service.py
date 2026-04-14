from openai import OpenAI
import os

# Set your API key (recommended via environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text: str):
    """
    AI Summarizer using OpenAI GPT model
    """

    if not text or text.strip() == "":
        return "Please provide text to summarize."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert text summarizer. Summarize the given text in simple and short form."
            },
            {
                "role": "user",
                "content": f"Summarize this text:\n\n{text}"
            }
        ],
        temperature=0.5,
        max_tokens=200
    )

    return response.choices[0].message.content