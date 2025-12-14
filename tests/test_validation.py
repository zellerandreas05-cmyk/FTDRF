import numpy as np

from ftdrf.simulator import simulate


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def test_kappa_zero_generates_fibonacci_sequence():
    # scalar case: psi0=1 (n=0), psi1=1 (n=1) -> psi_n == Fib(n+1)
    psi0 = np.array([1.0])
    psi1 = np.array([1.0])
    params = {"kappa": 0.0}
    seq = simulate(psi0, psi1, params, steps=10)
    # seq[0] is psi0 (n=0)
    for n, psi in enumerate(seq):
        expected = float(fib(n + 1))
        assert np.allclose(psi, expected)
