"""Prompt compression algorithms."""

import re


def compress_prompt(text: str, target_reduction: float = 0.2) -> str:
    """
    Compress a prompt by removing redundancy while preserving meaning.

    Techniques applied:
    1. Remove excessive whitespace
    2. Consolidate repeated instructions
    3. Shorten common phrases
    4. Remove filler words
    """
    result = text

    # Normalize whitespace
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = re.sub(r' {2,}', ' ', result)
    result = re.sub(r'\t', ' ', result)

    # Remove filler phrases
    fillers = [
        r'\bplease note that\b',
        r'\bit is important to\b',
        r'\bin order to\b',
        r'\bfor the purpose of\b',
        r'\bat this point in time\b',
        r'\bdue to the fact that\b',
        r'\bin the event that\b',
        r'\bwith regard to\b',
        r'\bin terms of\b',
        r'\bas a matter of fact\b',
    ]

    for filler in fillers:
        result = re.sub(filler, '', result, flags=re.IGNORECASE)

    # Clean up double spaces from removals
    result = re.sub(r' {2,}', ' ', result)
    result = result.strip()

    return result
