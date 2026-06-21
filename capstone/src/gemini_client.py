from typing import List, Optional
from .config import Config

class GeminiClient:
    """Interacts with Gemini LLM and Embedding endpoints (Skeleton)."""
    
    def __init__(self):
        # Configuration setup placeholder
        pass
        
    def generate_response(self, prompt: str, system_instruction: Optional[str] = None) -> str:
        """Generates text completion using the default model (stub)."""
        return "Stub response from Gemini client."
        
    def generate_embedding(self, text: str) -> List[float]:
        """Generates embedding vector using text-embedding endpoint (stub)."""
        return [0.0] * 768
