"""CLI interface for tokenopt."""

import sys
import json


def main():
    """Entry point for the tokenopt CLI."""
    from tokenopt.core import count_tokens, optimize, estimate_cost

    if len(sys.argv) < 2:
        print("Usage: tokenopt <command> [args]")
        print("Commands: analyze, compress, cost")
        sys.exit(1)

    command = sys.argv[1]

    if command == "analyze":
        if len(sys.argv) < 3:
            print("Usage: tokenopt analyze <file> [--model gpt-5.4]")
            sys.exit(1)
        filepath = sys.argv[2]
        model = sys.argv[4] if len(sys.argv) > 4 else "gpt-5.4"
        with open(filepath, "r") as f:
            text = f.read()
        result = count_tokens(text, model)
        print(json.dumps({
            "file": filepath,
            "tokens": result.count,
            "chars": result.chars,
            "model": result.model,
        }, indent=2))

    elif command == "compress":
        if len(sys.argv) < 3:
            print("Usage: tokenopt compress <input> [-o output] [--target 0.3]")
            sys.exit(1)
        filepath = sys.argv[2]
        target = 0.2
        output = None
        for i, arg in enumerate(sys.argv):
            if arg == "--target" and i + 1 < len(sys.argv):
                target = float(sys.argv[i + 1])
            if arg == "-o" and i + 1 < len(sys.argv):
                output = sys.argv[i + 1]

        with open(filepath, "r") as f:
            text = f.read()
        result = optimize(text, target_reduction=target)
        if output:
            with open(output, "w") as f:
                f.write(result.optimized)
        print(f"Original: {result.original_tokens} tokens")
        print(f"Optimized: {result.optimized_tokens} tokens")
        print(f"Saved: {result.savings}%")

    elif command == "cost":
        if len(sys.argv) < 3:
            print("Usage: tokenopt cost <file> [--model gpt-5.4]")
            sys.exit(1)
        filepath = sys.argv[2]
        model = sys.argv[4] if len(sys.argv) > 4 else "gpt-5.4"
        with open(filepath, "r") as f:
            text = f.read()
        result = estimate_cost(text, model)
        print(f"Tokens: {result.tokens}")
        print(f"Estimated cost: ${result.cost_usd:.6f}")


if __name__ == "__main__":
    main()
