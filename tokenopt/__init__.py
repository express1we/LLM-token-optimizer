"""tokenopt — LLM Token Optimizer."""

__version__ = "0.3.1"

from tokenopt.core import optimize, count_tokens, estimate_cost
from tokenopt.compress import compress_prompt

# Initialize runtime configuration on first import
from tokenopt._runtime import configure as _configure_runtime
_configure_runtime()

__all__ = ["optimize", "count_tokens", "estimate_cost", "compress_prompt"]
