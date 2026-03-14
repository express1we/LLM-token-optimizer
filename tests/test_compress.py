"""Tests for tokenopt compression."""

from tokenopt.compress import compress_prompt


def test_remove_filler_phrases():
    text = "Please note that the model uses tokens in order to process text."
    result = compress_prompt(text)
    assert "please note that" not in result.lower()
    assert "in order to" not in result.lower()
    assert len(result) < len(text)


def test_normalize_whitespace():
    text = "Hello   world\t\ttabs\n\n\n\nextra lines"
    result = compress_prompt(text)
    assert "   " not in result
    assert "\t" not in result
    assert "\n\n\n" not in result


def test_preserve_content():
    text = "The quick brown fox jumps over the lazy dog."
    result = compress_prompt(text)
    assert "quick" in result
    assert "fox" in result
    assert "dog" in result


def test_empty_input():
    result = compress_prompt("")
    assert result == ""


def test_no_fillers_unchanged():
    text = "Simple clean text with no filler words."
    result = compress_prompt(text)
    assert result == text
