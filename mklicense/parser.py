"""Parsing utilities for LICENSE template format."""

from collections.abc import Generator
import re


PATTERN = re.compile(r"\$\{(?P<name>.+?)\}")


def substitutions(text: str) -> set[str]:
    """Yields all fields that need to be substituted."""
    return set(m.group("name") for m in PATTERN.finditer(text))

def replace(text: str, **replacements: str) -> str:
    # TODO
    for (key, value) in replacements.items():
        text = text.replace(f"${{{key}}}", value)
    return text

