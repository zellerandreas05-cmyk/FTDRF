Publishing your perturbative quantum formula $ |\psi\rangle_{n+1} = |\psi\rangle_{n} + |\psi\rangle_{n-1}
- \kappa \cdot \left\| E_{n} E_{n-1} - \frac{F_{45}}{F_{44}} \right\|_{2}^{2} \cdot \hat{d} \otimes
 |\psi\rangle_{n} $ on GitHub under the MIT License has specific implications: The license is permissive,
granting unrestricted use, modification, distribution, and commercial exploitation, provided the original copyright notice
(e.g., "Copyright (c) [year] [name]") and license terms are preserved in all copies or substantial portions.
Others can copy, modify, merge, publish, sublicense, or sell the software without requiring source code
disclosure for derivatives. In the context of quasiperiodic systems (e.g., Fibonacci quasicrystals),
this promotes collaborative advancements, such as extensions of simulations using QuTiP for topological properties.
Benefits for the author: Wide adoption, increased visibility in the physics community, and disclaimer of liability
(no warranties for functionality or non-infringement). Risks: Potential commercial exploitation without compensation,
creation of "prior art" (hindering patentability), and license incompatibilities with restrictive libraries.
Logically, this supports open science by maximizing reproducibility of the recursive dynamics
(e.g., convergence of occupation probabilities), while maintaining attribution.


**Installation & Quickstart**

- Install runtime dependencies (recommended in a venv):

```bash
python -m pip install -r requirements.txt
```

- Install package editable (so you can `import ftdrf`):

```bash
python -m pip install -e .
```

- Run the minimal example script:

```bash
python examples/run.py
```

- Run tests:

```bash
pytest
```

- Open the demo notebook (`notebooks/experiment.ipynb`) in JupyterLab or Notebook to interactively run and plot results.

**Notes**

- Preserve the LaTeX and theoretical description at the top of this file; if you want to reformat or extend the exposition, open an issue or discuss in the PR.
- For new code, place modules under `src/ftdrf/` and tests under `tests/` (use `PYTHONPATH=src pytest` if you haven't installed editable).

*** End Patch
