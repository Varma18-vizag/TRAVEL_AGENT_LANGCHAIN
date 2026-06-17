from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

load_dotenv()

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"


def generate_response(prompt: str) -> str:

    response = client.chat_completion(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
