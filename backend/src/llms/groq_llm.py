from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

class GroqModel:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            llm = ChatGroq(api_key= self.groq_api_key, model= "openai/gpt-oss-20b")
            return llm
        except Exception as e:
            raise ValueError(f"Exception caught: {e}")