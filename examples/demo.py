#!/usr/bin/env python3
"""Quick demo of tokenopt capabilities."""

from tokenopt import optimize, count_tokens, estimate_cost
from tokenopt.compress import compress_prompt


def main():
    sample = """
    Please note that it is important to understand that in order to
    effectively utilize large language models, one must be mindful of
    token usage. Due to the fact that API costs are calculated on a
    per-token basis, it is important to optimize prompts. At this point
    in time, many developers are not aware of how many tokens their
    prompts consume, and for the purpose of reducing costs, tools like
    tokenopt can help analyze and compress prompts automatically.
    """

    print("=" * 60)
    print("tokenopt Demo — LLM Token Optimizer")
    print("=" * 60)

    # 1. Count tokens
    print("\n1. Token Counting")
    print("-" * 40)
    for model in ["gpt-5.4", "gpt-5.3-codex", "gemini-2.5-pro"]:
        result = count_tokens(sample, model)
        print(f"  {model}: {result.count} tokens ({result.chars} chars)")

    # 2. Optimize prompt
    print("\n2. Prompt Optimization")
    print("-" * 40)
    result = optimize(sample, model="gpt-5.4", target_reduction=0.3)
    print(f"  Original:  {result.original_tokens} tokens")
    print(f"  Optimized: {result.optimized_tokens} tokens")
    print(f"  Saved:     {result.savings}%")

    # 3. Cost estimation
    print("\n3. Cost Estimation")
    print("-" * 40)
    for model in ["gpt-5.4", "gpt-5.1-codex-mini", "o4-mini"]:
        result = estimate_cost(sample, model)
        print(f"  {model}: ${result.cost_usd:.6f} ({result.tokens} tokens)")

    # 4. Direct compression
    print("\n4. Compression Preview")
    print("-" * 40)
    compressed = compress_prompt(sample)
    print(f"  Before: {len(sample)} chars")
    print(f"  After:  {len(compressed)} chars")
    print(f"  Ratio:  {len(compressed)/len(sample)*100:.1f}%")

    print("\n" + "=" * 60)
    print("Done! See README.md for full API and CLI usage.")
    print("=" * 60)


if __name__ == "__main__":
    main()
