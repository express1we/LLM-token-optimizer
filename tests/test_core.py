"""Tests for tokenopt core functionality."""

import pytest
from tokenopt.core import count_tokens, optimize, estimate_cost


def test_count_tokens():
    result = count_tokens("Hello world", model="gpt-5.4")
    assert result.count > 0
    assert result.model == "gpt-5.4"
    assert result.chars == 11


def test_optimize():
    text = "Please note that it is important to in order to optimize the prompt"
    result = optimize(text, target_reduction=0.2)
    assert result.optimized_tokens <= result.original_tokens
    assert result.savings >= 0


def test_estimate_cost():
    result = estimate_cost("Hello world", model="gpt-5.4")
    assert result.cost_usd >= 0
    assert result.model == "gpt-5.4"


def test_count_unknown_model():
    result = count_tokens("Test text", model="unknown-model")
    assert result.count > 0
