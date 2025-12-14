"""Small simulator utilities for the FTDRF recurrence.

Provides a `step` function implementing the recurrence roughly as described in
`README.md` and a simple `simulate` helper to run N steps.

The implementation keeps things intentionally simple and generic:
- `psi` are 1D numpy arrays (vectors)
- `d_hat` may be a scalar, a vector (elementwise multiply), or a matrix (applied with `@`)
- `E_n`, `E_nm1`, `F45`, `F44` may be scalars or arrays; norm is computed with `np.linalg.norm`
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List

import numpy as np


def _compute_norm_term(E_n: Any, E_nm1: Any, F45: Any, F44: Any) -> float:
    diff = E_n * E_nm1 - (F45 / F44)
    arr = np.asarray(diff)
    if arr.size == 1:
        val = float(abs(arr))
    else:
        val = float(np.linalg.norm(arr))
    return val * val


def _apply_d_hat(d_hat: Any, psi: np.ndarray) -> np.ndarray:
    if np.isscalar(d_hat):
        return d_hat * psi
    arr = np.asarray(d_hat)
    if arr.ndim == 1 and arr.size == psi.size:
        return arr * psi
    if arr.ndim == 2 and arr.shape[1] == psi.size:
        return arr @ psi
    raise ValueError("d_hat must be scalar, 1D vector (same size as psi) or 2D operator")


def step(psi_n: np.ndarray, psi_nm1: np.ndarray, params: Dict[str, Any]) -> np.ndarray:
    """Compute the next state `psi_{n+1}` from `psi_n` and `psi_{n-1}`.

    Parameters
    - psi_n, psi_nm1: 1D numpy arrays (same shape)
    - params: dict with keys:
        - `kappa` (float)
        - `E_n`, `E_nm1`, `F45`, `F44` (scalars or arrays)
        - `d_hat` (scalar, vector, or matrix)

    Returns
    - psi_next: 1D numpy array
    """
    psi_n = np.asarray(psi_n)
    psi_nm1 = np.asarray(psi_nm1)
    if psi_n.shape != psi_nm1.shape:
        raise ValueError("psi_n and psi_nm1 must have same shape")

    kappa = float(params.get("kappa", 1.0))
    E_n = params.get("E_n", 0.0)
    E_nm1 = params.get("E_nm1", 0.0)
    F45 = params.get("F45", 0.0)
    F44 = params.get("F44", 1.0)
    d_hat = params.get("d_hat", 1.0)

    norm_term = _compute_norm_term(E_n, E_nm1, F45, F44)
    op_term = _apply_d_hat(d_hat, psi_n)
    psi_next = psi_n + psi_nm1 - kappa * norm_term * op_term
    return np.asarray(psi_next)


def simulate(psi0: np.ndarray, psi1: np.ndarray, params: Dict[str, Any], steps: int) -> List[np.ndarray]:
    """Run `steps` iterations starting from `psi0` (n=0) and `psi1` (n=1).

    Returns list: [psi0, psi1, psi2, ..., psiN]
    """
    psi0 = np.asarray(psi0)
    psi1 = np.asarray(psi1)
    seq = [psi0, psi1]
    for _ in range(steps):
        nxt = step(seq[-1], seq[-2], params)
        seq.append(nxt)
    return seq
