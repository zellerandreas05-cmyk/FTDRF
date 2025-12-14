"""Parameter scan and validation utilities for FTDRF.

Generates a simple plot of ||psi|| over steps for different kappa values.
"""

import os
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np

from ftdrf.simulator import simulate


def run_scan(kappas: Sequence[float], steps: int = 50, outdir: str = "examples/figures") -> None:
    os.makedirs(outdir, exist_ok=True)
    psi0 = np.array([1.0])
    psi1 = np.array([1.0])
    for k in kappas:
        params = {"kappa": k, "E_n": 1.0, "E_nm1": 0.8, "F45": 0.1, "F44": 1.0, "d_hat": 1.0}
        seq = simulate(psi0, psi1, params, steps=steps)
        norms = [np.linalg.norm(s) for s in seq]
        plt.plot(norms, label=f"kappa={k}")
    plt.xlabel("n")
    plt.ylabel("||psi||")
    plt.legend()
    out = os.path.join(outdir, "kappa_scan.png")
    plt.savefig(out)
    plt.clf()
    print(f"Saved scan to {out}")


if __name__ == "__main__":
    run_scan([0.0, 0.1, 0.5, 1.0], steps=100)
