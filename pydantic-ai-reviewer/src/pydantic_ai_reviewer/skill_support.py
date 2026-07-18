from __future__ import annotations

import importlib.util
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parents[2] / "skills"
_LINKEDIN_RETRIEVER_PATH = SKILLS_DIR / "screen-candidate" / "scripts" / "linked_in_retriever.py"

_spec = importlib.util.spec_from_file_location(
    "pydantic_ai_reviewer_skill_linked_in_retriever",
    _LINKEDIN_RETRIEVER_PATH,
)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Could not load skill retriever module from {_LINKEDIN_RETRIEVER_PATH}")

_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

retrieve_linkedin_profile = _module.get_linkedin_profile
