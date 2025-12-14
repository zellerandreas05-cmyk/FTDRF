import numpy as np
from hypothesis import given, strategies as st

from ftdrf.simulator import step


@given(
    psi0=st.lists(st.floats(-10, 10), min_size=1, max_size=5),
    psi1=st.lists(st.floats(-10, 10), min_size=1, max_size=5),
    kappa=st.floats(0, 5),
)
def test_step_shape_and_deterministic(psi0, psi1, kappa):
    # ensure same shape and determinism
    import numpy as np

    psi0 = np.asarray(psi0, dtype=float)
    psi1 = np.asarray(psi1, dtype=float)
    if psi0.shape != psi1.shape:
        # skip mismatched shapes in this property (we already test shape mismatch elsewhere)
        return
    params = {"kappa": float(kappa), "E_n": 1.0, "E_nm1": 1.0, "F45": 0.1, "F44": 1.0, "d_hat": 0.5}
    out1 = step(psi1, psi0, params)
    out2 = step(psi1, psi0, params)
    assert out1.shape == psi0.shape
    assert np.allclose(out1, out2)


@given(
    psi0=st.lists(st.floats(-5, 5), min_size=1, max_size=5),
    psi1=st.lists(st.floats(-5, 5), min_size=1, max_size=5),
    kappa=st.floats(0, 10),
)
def test_d_hat_zero_reduces_to_sum(psi0, psi1, kappa):
    # If d_hat is zero, psi_{n+1} == psi_n + psi_{n-1} regardless of kappa
    import numpy as np

    psi0 = np.asarray(psi0, dtype=float)
    psi1 = np.asarray(psi1, dtype=float)
    if psi0.shape != psi1.shape:
        return
    params = {"kappa": float(kappa), "E_n": 2.0, "E_nm1": 3.0, "F45": 0.2, "F44": 1.0, "d_hat": 0.0}
    out = step(psi1, psi0, params)
    assert np.allclose(out, psi1 + psi0)
