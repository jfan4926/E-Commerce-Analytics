import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pages.ab_test import bayesian_ab_test


def test_b_clearly_better():
    """B better, P(B>A) should approach 1"""
    result = bayesian_ab_test(
        a_trials=1000, a_success=500,   # A: 50%
        b_trials=1000, b_success=900,   # B: 90%
    )
    assert result["prob_b_better"] > 0.99


def test_a_clearly_better():
    """A better, P(B>A) should approach 0"""
    result = bayesian_ab_test(
        a_trials=1000, a_success=900,   # A: 90%
        b_trials=1000, b_success=500,   # B: 50%
    )
    assert result["prob_b_better"] < 0.01


def test_similar_groups():
    """when both close, P(B>A) should lie between 0.3~0.7 """
    result = bayesian_ab_test(
        a_trials=1000, a_success=500,
        b_trials=1000, b_success=510,
    )
    assert 0.3 < result["prob_b_better"] < 0.7


def test_rates_correct():
    """make sure a_rate & b_rate are calculated correctly"""
    result = bayesian_ab_test(
        a_trials=1000, a_success=300,
        b_trials=1000, b_success=700,
    )
    assert abs(result["a_rate"] - 0.3) < 0.001
    assert abs(result["b_rate"] - 0.7) < 0.001


def test_credible_intervals():
    """95% credible interval should contain credible intervals"""
    result = bayesian_ab_test(
        a_trials=10000, a_success=6000,  # about 60%
        b_trials=10000, b_success=7000,  # about 70%
    )
    assert result["a_ci"][0] < 0.60 < result["a_ci"][1]
    assert result["b_ci"][0] < 0.70 < result["b_ci"][1]