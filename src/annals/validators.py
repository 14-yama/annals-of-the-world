"""Basic QA validators used by the curator workflow.

These are simple, local checks that can be run before publishing nodes.
"""
from typing import Iterable, Dict


def check_active_voice_relationships(rel_names: Iterable[str]) -> Dict[str, bool]:
    """Return a map of relationship name -> True if active-voice, False if passive-ish.

    This is a heuristic check: it flags names that look passive (ending with _BY or starting with 'IS_').
    """
    results = {}
    for r in rel_names:
        name = r.upper()
        if name.endswith("_BY") or name.startswith("IS_") or "_BY_" in name:
            results[r] = False
        else:
            results[r] = True
    return results


def requires_framed_by(node_props: Dict) -> bool:
    """Return True if a node (or relation payload) appears to have required FRAMED_BY metadata.

    Basic heuristic: check for a 'framed_by' key or 'citation_style' presence.
    """
    if not isinstance(node_props, dict):
        return False
    return bool(node_props.get("framed_by") or node_props.get("citation_style"))
