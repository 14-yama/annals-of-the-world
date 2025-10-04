from neo4j import GraphDatabase
from .config import get_config


def get_neo4j_driver():
    """Return a Neo4j driver using repository config."""
    cfg = get_config()
    return GraphDatabase.driver(cfg.NEO4J_URI, auth=(cfg.NEO4J_USER, cfg.NEO4J_PASSWORD))
