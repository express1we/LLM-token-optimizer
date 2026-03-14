"""Tests for tokenopt API endpoints."""

import pytest
from fastapi.testclient import TestClient
from tokenopt.api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "0.3.1"


def test_count_endpoint():
    response = client.post("/count", json={
        "text": "Hello world, this is a test.",
        "model": "gpt-5.4",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["tokens"] > 0
    assert data["model"] == "gpt-5.4"


def test_optimize_endpoint():
    response = client.post("/optimize", json={
        "text": "Please note that it is important to in order to process the data.",
        "model": "gpt-5.4",
        "target_reduction": 0.2,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["optimized_tokens"] <= data["original_tokens"]
    assert "savings_percent" in data


def test_estimate_endpoint():
    response = client.post("/estimate", json={
        "text": "Hello world",
        "model": "gpt-5.4",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["cost_usd"] >= 0
    assert data["model"] == "gpt-5.4"
