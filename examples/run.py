"""Minimal runnable example to demonstrate `src/ftdrf/simulator.py`.

Run with: python examples/run.py
"""

import numpy as np

from ftdrf.simulator import simulate


def main() -> None:
    psi0 = np.array([1.0, 0.0])
    psi1 = np.array([0.0, 1.0])
    params = {"kappa": 0.5, "E_n": 1.0, "E_nm1": 0.8, "F45": 0.1, "F44": 1.0, "d_hat": np.array([1.0, 1.0])}
    seq = simulate(psi0, psi1, params, steps=10)
    norms = [np.linalg.norm(s) for s in seq]
    for i, n in enumerate(norms):
        print(f"n={i}: norm={n:.6f}")


if __name__ == "__main__":
    main()
