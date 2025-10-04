"""Simple Neo4j client helpers.

This is a minimal safe wrapper around the official neo4j driver.
"""
from typing import Any, Dict, Iterable, List, Optional
from neo4j import GraphDatabase, Driver, Session
from neo4j.exceptions import Neo4jError
from .config import get_config


class Neo4jClient:
    def __init__(self, config=None):
        self.config = config or get_config()
        self._driver: Optional[Driver] = None

    def get_driver(self) -> Driver:
        if self._driver is None:
            uri = self.config.NEO4J_URI
            user = self.config.NEO4J_USER
            password = self.config.NEO4J_PASSWORD
            self._driver = GraphDatabase.driver(uri, auth=(user, password))
        return self._driver

    def close(self) -> None:
        if self._driver:
            self._driver.close()
            self._driver = None

    def run_query(self, cypher: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Run a read query and return results as list of dicts.

        Uses a read transaction by default; for write queries use explicit transactions.
        """
        params = params or {}
        driver = self.get_driver()
        try:
            with driver.session(database=self.config.NEO4J_DATABASE) as session:
                # neo4j result records expose data() to get a dict
                # session.run typing is strict; runtime accepts str - silence static checker
                result = session.run(cypher, **params)  # type: ignore[arg-type]
                return [rec.data() for rec in result]
        except Neo4jError:
            # re-raise for caller to handle; keep wrapper minimal
            raise


def run_query_raw(cypher: str, params: Optional[Dict[str, Any]] = None):
    client = Neo4jClient()
    try:
        return client.run_query(cypher, params)
    finally:
        client.close()
