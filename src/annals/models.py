from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel, Field


# ── Sub-models for structured nested data ──

class CauseEffect(BaseModel):
    title: str
    type: str
    year: str
    slug: Optional[str] = None
    direction: str = Field(..., description="'cause' or 'effect'")


class Relationship(BaseModel):
    source_slug: str
    source_name: str
    verb: str
    target_slug: str
    target_name: str
    context: Optional[str] = None


class PlaceRef(BaseModel):
    name: str
    role: str
    slug: Optional[str] = None


class TextRef(BaseModel):
    title: str
    type: str
    year: Optional[str] = None
    slug: Optional[str] = None


class BaseNode(BaseModel):
    slug: str = Field(..., description="Canonical short id; unique per label")
    name: Optional[str]
    description: Optional[str]
    summary: Optional[str] = None
    created_at: Optional[str]
    updated_at: Optional[str]
    created_by: Optional[str]
    status: Optional[str]
    # v4+ registry fields
    alt_names: Optional[List[str]] = None
    category: Optional[str] = None
    class_number: Optional[str] = None
    division_code: Optional[str] = None
    call_number: Optional[str] = None
    subject_headings: Optional[List[str]] = None
    subjects: Optional[List[str]] = None
    is_generic: Optional[bool] = None
    intl_status: Optional[str] = None
    status_by: Optional[str] = None
    version: Optional[int] = None
    corpus: Optional[List[str]] = None
    lang: Optional[str] = None
    script: Optional[str] = None
    # Geographic / era context (shared across all node types)
    era: Optional[str] = None
    era_slug: Optional[str] = None
    region: Optional[str] = None
    continent: Optional[str] = None
    # Frameworks
    frameworks: Optional[List[str]] = None
    # v5-ready additions
    source_origin: Optional[str] = None
    source_id: Optional[str] = None
    reviewed_by: Optional[List[str]] = None
    review_date: Optional[str] = None
    deprecated_reason: Optional[str] = None
    external_links: Optional[List[str]] = None
    ontology_class: Optional[str] = None
    thesaurus_ref: Optional[str] = None
    wikidata_qid: Optional[str] = None
    wikipedia_url: Optional[str] = None
    schema_context: Optional[str] = None
    importance_score: Optional[float] = None
    citation_count: Optional[int] = None
    connectedness: Optional[float] = None
    review_status: Optional[str] = None
    qa_notes: Optional[str] = None
    cultural_context: Optional[str] = None
    translation_status: Optional[str] = None
    translators: Optional[List[str]] = None
    orthography_note: Optional[str] = None
    midYear: Optional[int] = None
    duration: Optional[int] = None
    periodic_overlap: Optional[List[str]] = None
    spatial_extent: Optional[str] = None
    geo_precision: Optional[str] = None
    isbn: Optional[str] = None
    issn: Optional[str] = None
    edition: Optional[str] = None
    pages_total: Optional[int] = None
    license: Optional[str] = None
    workflow_stage: Optional[str] = None
    governance_version: Optional[int] = None
    validation_hash: Optional[str] = None
    display_label: Optional[str] = None
    era_ref: Optional[str] = None
    citation_density: Optional[int] = None
    has_geo: Optional[bool] = None
    has_text: Optional[bool] = None
    # v2 enrichment fields
    image_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    tags: Optional[List[str]] = None
    quote: Optional[str] = None
    legacy_summary: Optional[str] = None


class Idea(BaseNode):
    idea_index: Optional[int] = None


class Person(BaseNode):
    birthYear: Optional[int] = None
    deathYear: Optional[int] = None
    born: Optional[str] = None
    died: Optional[str] = None
    titles: Optional[List[str]] = None
    aliases: Optional[List[str]] = None


class Place(BaseNode):
    kind: Optional[str] = None
    region: Optional[str] = None
    geo_lat: Optional[float] = None
    geo_lon: Optional[float] = None
    iso: Optional[str] = None


class EventWindow(BaseNode):
    startYear: Optional[int] = None
    endYear: Optional[int] = None
    chron_key: Optional[int] = None
    context: Optional[str] = None
    confidence_score: Optional[float] = None
    summary: Optional[str] = None
    significance: Optional[str] = None
    score: Optional[float] = None
    tags: Optional[List[str]] = None


class Evidence(BaseNode):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    publisher: Optional[str] = None
    doi_or_url: Optional[str] = None
    lang: Optional[str] = None
    script: Optional[str] = None
    corpus_tier: Optional[str] = None


class Corpus(BaseNode):
    corpus_tier: Optional[str] = None


class Framework(BaseNode):
    code: Optional[str] = None
    category: Optional[str] = None
    definition: Optional[str] = None
    notes: Optional[str] = None


__all__ = [
    "CauseEffect",
    "Relationship",
    "PlaceRef",
    "TextRef",
    "BaseNode",
    "Idea",
    "Person",
    "Place",
    "EventWindow",
    "Evidence",
    "Corpus",
    "Framework",
]
