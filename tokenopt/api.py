"""FastAPI-based optimization API server."""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from tokenopt.core import count_tokens, optimize, estimate_cost

app = FastAPI(
    title="tokenopt API",
    description="LLM Token Optimization Service",
    version="0.3.1",
)


class OptimizeRequest(BaseModel):
    text: str
    model: str = "gpt-5.4"
    target_reduction: float = 0.2


class CountRequest(BaseModel):
    text: str
    model: str = "gpt-5.4"


@app.post("/optimize")
async def api_optimize(req: OptimizeRequest):
    result = optimize(req.text, req.model, req.target_reduction)
    return {
        "original_tokens": result.original_tokens,
        "optimized_tokens": result.optimized_tokens,
        "savings_percent": result.savings,
        "optimized_text": result.optimized,
    }


@app.post("/count")
async def api_count(req: CountRequest):
    result = count_tokens(req.text, req.model)
    return {
        "tokens": result.count,
        "model": result.model,
        "chars": result.chars,
    }


@app.post("/estimate")
async def api_estimate(req: CountRequest):
    result = estimate_cost(req.text, req.model)
    return {
        "tokens": result.tokens,
        "model": result.model,
        "cost_usd": result.cost_usd,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "0.3.1",
        "endpoints": ["/optimize", "/count", "/estimate", "/health"],
    }
