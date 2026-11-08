#!/usr/bin/env python3
"""
Shared xAI Grok (OpenAI-compatible) client for Annals local bots.

Env (never logged):
  XAI_API_KEY or GROK_API_KEY — Bearer token from https://console.x.ai
  GROK_MODEL — default grok-4.7
  XAI_BASE_URL — default https://api.x.ai/v1

Usage:
  from llm_grok import resolve_grok_api_key, call_grok_json, call_grok_json_list
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


DEFAULT_MODEL = os.environ.get("GROK_MODEL", "grok-4.7")
DEFAULT_BASE = os.environ.get("XAI_BASE_URL", "https://api.x.ai/v1").rstrip("/")


def resolve_grok_api_key() -> str:
    """Return XAI_API_KEY or GROK_API_KEY (empty if unset). Never print the value."""
    return (
        os.environ.get("XAI_API_KEY", "").strip()
        or os.environ.get("GROK_API_KEY", "").strip()
    )


def grok_configured() -> bool:
    return bool(resolve_grok_api_key())


def _parse_json_object(text: str) -> dict:
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass
    s = text.find("{")
    e = text.rfind("}")
    if s >= 0 and e > s:
        return json.loads(text[s : e + 1])
    raise json.JSONDecodeError("no JSON object", text, 0)


def _parse_json_list(text: str) -> list:
    try:
        data = json.loads(text)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in ("edges", "relationships", "items", "data"):
                if isinstance(data.get(key), list):
                    return data[key]
    except json.JSONDecodeError:
        pass
    s = text.find("[")
    e = text.rfind("]")
    if s >= 0 and e > s:
        data = json.loads(text[s : e + 1])
        if isinstance(data, list):
            return data
    raise json.JSONDecodeError("no JSON array", text, 0)


def call_grok_chat(
    prompt: str,
    *,
    api_key: str | None = None,
    model: str | None = None,
    system: str = (
        "You are a historical knowledge base enrichment assistant. "
        "Return ONLY valid JSON matching the requested schema."
    ),
    temperature: float = 0.7,
    timeout: int = 120,
) -> str:
    """Raw chat completion content string from xAI Grok."""
    key = (api_key or resolve_grok_api_key()).strip()
    if not key:
        raise RuntimeError(
            "XAI_API_KEY / GROK_API_KEY not set — add to ~/.config/annals/env or repo .env"
        )
    model_name = model or DEFAULT_MODEL
    url = f"{DEFAULT_BASE}/chat/completions"
    body = json.dumps(
        {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "temperature": temperature,
            # Prefer JSON object; some Grok models honor this OpenAI-compatible field.
            "response_format": {"type": "json_object"},
        }
    ).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", errors="replace")[:300]
        except Exception:
            pass
        raise RuntimeError(f"Grok HTTP {exc.code}: {detail or exc.reason}") from exc

    choices = data.get("choices") or []
    if not choices:
        raise RuntimeError("Grok returned no choices")
    msg = choices[0].get("message") or {}
    text = msg.get("content") or ""
    if not isinstance(text, str) or not text.strip():
        raise RuntimeError("Grok returned empty content")
    return text


def call_grok_json(
    prompt: str,
    *,
    api_key: str | None = None,
    model: str | None = None,
    system: str | None = None,
    temperature: float = 0.7,
) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "api_key": api_key,
        "model": model,
        "temperature": temperature,
    }
    if system is not None:
        kwargs["system"] = system
    text = call_grok_chat(prompt, **kwargs)
    return _parse_json_object(text)


def call_grok_json_list(
    prompt: str,
    *,
    api_key: str | None = None,
    model: str | None = None,
    temperature: float = 0.4,
) -> list:
    system = (
        "You are a historical knowledge graph edge generator. "
        "Return ONLY a JSON array of edge objects."
    )
    # Arrays: skip response_format json_object — ask for array in prompt.
    key = (api_key or resolve_grok_api_key()).strip()
    if not key:
        raise RuntimeError(
            "XAI_API_KEY / GROK_API_KEY not set — add to ~/.config/annals/env or repo .env"
        )
    model_name = model or DEFAULT_MODEL
    url = f"{DEFAULT_BASE}/chat/completions"
    body = json.dumps(
        {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "temperature": temperature,
        }
    ).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    text = (data.get("choices") or [{}])[0].get("message", {}).get("content") or ""
    return _parse_json_list(text)
