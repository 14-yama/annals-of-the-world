from dataclasses import dataclass
import os

# load_dotenv if available; tolerate missing dependency at static-check time
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    # dotenv not installed in static analysis environment; proceed without it
    def load_dotenv():
        return False



@dataclass
class Config:
    NEO4J_URI: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "")
    NEO4J_DATABASE: str = os.getenv("NEO4J_DATABASE", "neo4j")


def get_config() -> Config:
    """Return a Config instance loaded from environment variables."""
    return Config()
