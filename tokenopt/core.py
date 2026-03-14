"""Core token counting and optimization functions."""

from dataclasses import dataclass
from typing import Optional


# Approximate token ratios for different models
MODEL_RATIOS = {
    "gpt-5.4": 0.75,
    "gpt-5.3-codex": 0.75,
    "gpt-5.2-codex": 0.75,
    "gpt-5.2": 0.75,
    "gpt-5.1-codex-max": 0.75,
    "gpt-5.1-codex-mini": 0.75,
    "o4-mini": 0.75,
    "o3": 0.75,
    "gemini-2.5-pro": 0.72,
    "gemini-2.5-flash": 0.72,
    "llama-4-maverick": 0.70,
    "deepseek-r1": 0.73,
}

# Cost per 1K tokens (input) in USD
MODEL_COSTS = {
    "gpt-5.4": 0.005,
    "gpt-5.3-codex": 0.003,
    "gpt-5.2-codex": 0.002,
    "gpt-5.2": 0.002,
    "gpt-5.1-codex-max": 0.0015,
    "gpt-5.1-codex-mini": 0.0004,
    "o4-mini": 0.0011,
    "o3": 0.01,
    "gemini-2.5-pro": 0.00125,
    "gemini-2.5-flash": 0.00015,
    "llama-4-maverick": 0.0002,
    "deepseek-r1": 0.00055,
}


@dataclass
class TokenResult:
    """Result of token counting."""
    count: int
    model: str
    chars: int
    ratio: float


@dataclass
class OptimizeResult:
    """Result of prompt optimization."""
    original: str
    optimized: str
    original_tokens: int
    optimized_tokens: int
    savings: float


@dataclass
class CostEstimate:
    """Cost estimation result."""
    tokens: int
    model: str
    cost_usd: float


def count_tokens(text: str, model: str = "gpt-5.4") -> TokenResult:
    """Count tokens for a given text and model."""
    try:
        import tiktoken
        enc = tiktoken.encoding_for_model(model)
        tokens = len(enc.encode(text))
    except (ImportError, KeyError):
        ratio = MODEL_RATIOS.get(model, 0.75)
        tokens = int(len(text.split()) / ratio)

    return TokenResult(
        count=tokens,
        model=model,
        chars=len(text),
        ratio=tokens / max(len(text), 1),
    )


def optimize(text: str, model: str = "gpt-5.4",
             target_reduction: float = 0.2) -> OptimizeResult:
    """Optimize a prompt to reduce token usage."""
    from tokenopt.compress import compress_prompt

    original_count = count_tokens(text, model).count
    optimized_text = compress_prompt(text, target_reduction)
    optimized_count = count_tokens(optimized_text, model).count

    savings = (1 - optimized_count / max(original_count, 1)) * 100

    return OptimizeResult(
        original=text,
        optimized=optimized_text,
        original_tokens=original_count,
        optimized_tokens=optimized_count,
        savings=round(savings, 1),
    )


def estimate_cost(text: str, model: str = "gpt-5.4") -> CostEstimate:
    """Estimate API cost for the given text."""
    tokens = count_tokens(text, model).count
    cost_per_k = MODEL_COSTS.get(model, 0.01)
    cost = (tokens / 1000) * cost_per_k

    return CostEstimate(
        tokens=tokens,
        model=model,
        cost_usd=round(cost, 6),
    )
