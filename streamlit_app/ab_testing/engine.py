import numpy as np


def bayesian_ab_test(a_trials, a_success, b_trials, b_success, n_samples=50000):
    a_dist = np.random.beta(a_success + 1, a_trials - a_success + 1, n_samples)
    b_dist = np.random.beta(b_success + 1, b_trials - b_success + 1, n_samples)
    return {
        "prob_b_better":   float((b_dist > a_dist).mean()),
        "relative_uplift": float((b_dist.mean() - a_dist.mean()) / a_dist.mean() * 100),
        "a_rate": a_success / a_trials,
        "b_rate": b_success / b_trials,
        "a_ci":   np.percentile(a_dist, [2.5, 97.5]),
        "b_ci":   np.percentile(b_dist, [2.5, 97.5]),
        "a_samples": a_dist,
        "b_samples": b_dist,
    }