# tokenopt — LLM Token Optimizer

A lightweight CLI and library for analyzing, compressing, and optimizing prompts to reduce token usage across OpenAI and Google models.

## Features

- **Token counting** — Accurate token counts for GPT-5.4, GPT-5.3-Codex, Gemini 2.5, Llama 4, DeepSeek
- **Prompt compression** — Reduce token usage by 20-40% without quality loss
- **Batch optimization** — Process prompt datasets in bulk
- **Cost estimation** — Estimate API costs before sending
- **CI integration** — GitHub Actions support for prompt regression testing

## Quick Start

```bash
# Clone and set up
git clone https://github.com/express1we/LLM-token-optimizer.git
cd LLM-token-optimizer

# Windows
setup.bat

# macOS / Linux
chmod +x setup.sh && ./setup.sh
```

## Usage

```python
from tokenopt import optimize, count_tokens

# Count tokens
result = count_tokens("Your prompt here", model="gpt-5.4")
print(f"Tokens: {result.count}")

# Optimize prompt
optimized = optimize("Your long verbose prompt...", target_reduction=0.3)
print(f"Saved {optimized.savings}% tokens")
```

## CLI

```bash
# Analyze a prompt file
tokenopt analyze prompt.txt --model gpt-5.4

# Optimize and save
tokenopt compress input.txt -o output.txt --target 0.3

# Batch process
tokenopt batch prompts/ --output optimized/ --report costs.json
```

## License

MIT
