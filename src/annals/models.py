from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel, Field


class BaseNode(BaseModel):
    slug: str = Field(..., description="Canonical short id; unique per label")
    name: Optional[str]
    description: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    created_by: Optional[str]
    status: Optional[str]


class Idea(BaseNode):
    category: Optional[str]
    is_generic: Optional[bool] = False


class Person(BaseNode):
    category: Optional[str]
    birth_year: Optional[int]
    death_year: Optional[int]


class Place(BaseNode):
    place_type: Optional[str]
    region: Optional[str]


class EventWindow(BaseNode):
    startYear: Optional[int]
    endYear: Optional[int]
    chron_key: Optional[int]
    place_slug: Optional[str]


class Evidence(BaseNode):
    evidence_url: Optional[str]
    citation_style: Optional[str]
    page_refs: Optional[str]
    corpus: Optional[str]
    corpus_tier: Optional[str]


class Corpus(BaseNode):
    tier: Optional[str]


class Framework(BaseNode):
    framework_type: Optional[str]


__all__ = [
    "BaseNode",
    "Idea",
    "Person",
    "Place",
    "EventWindow",
    "Evidence",
    "Corpus",
    "Framework",
]
