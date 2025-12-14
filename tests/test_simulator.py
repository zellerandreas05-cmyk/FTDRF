import numpy as np

from ftdrf.simulator import step, simulate


def test_zero_state_is_stable():
    psi0 = np.zeros(4)
    psi1 = np.zeros(4)
    params = {"kappa": 1.0}
    nxt = step(psi1, psi0, params)
    assert np.allclose(nxt, 0)


def test_kappa_zero_reduces_to_linear_sum():
    psi0 = np.array([1.0, 2.0])
    psi1 = np.array([0.5, -1.0])
    params = {"kappa": 0.0}
    nxt = step(psi1, psi0, params)
    assert np.allclose(nxt, psi1 + psi0)


def test_simulate_length_and_shapes():
    psi0 = np.zeros(3)
    psi1 = np.ones(3)
    params = {"kappa": 0.0}
    seq = simulate(psi0, psi1, params, steps=5)
    assert len(seq) == 7  # psi0 + psi1 + 5 steps
    for arr in seq:
        assert arr.shape == psi0.shape
