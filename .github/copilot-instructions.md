<!-- .github/copilot-instructions.md for FTDRF -->
# Copilot / AI Agent Instructions — FTDRF

Purpose
- Short: Help an AI coding agent become immediately productive in this repository.
- Current repo state: single top-level file `[README.md](README.md)` containing a LaTeX/physics description of the Fibonacci Threshold Dyadic Recursive Filter and its core recursive equation for |ψ⟩. Do not remove or alter the LaTeX without confirming with the maintainer.

Big picture
- This repository presently contains research notes (not an application). The README encodes the core mathematical model: a recursive update rule for |ψ⟩ (see the equation in `README.md`).
- Any code additions should implement or reproduce the mathematical model and numerical experiments described in the README; expect a research-style workspace (simulations, notebooks, small scripts).

Primary goals for an AI agent
- Propose minimal, well-scoped changes (e.g., add a simulation script and a short Jupyter notebook demonstrating results).
- Make pull requests small and focused; include runnable examples and tests that validate numerical behavior (convergence, conservation laws, or reproducing a small known case).

Where to add code and tests
- New code: create a `src/` package (prefer short, descriptive names) and a `notebooks/` folder for interactive exploration.
- Tests: add `tests/` for unit and integration tests using `pytest` so CI (if added) can run them.

> Examples
- Implement a small Python module `src/ftdrf/simulator.py` with a function `step(psi_n, psi_n_minus1, params)` reflecting the README formula.
- Add `notebooks/experiment.ipynb` that reproduces a short sequence of iterations and plots norms/observables.

Conventions & safety
- Preserve the academic content: maintain the README's LaTeX and introductory text. If you propose reformatting or expanding the README, explain why and show the diff in your PR.
- Don't add heavy infra (containers, elaborate CI) without maintainers' sign-off—this is a small research repo.

Developer workflows (when you add them)
- Prefer Python 3.11+ and standard tooling: `pytest` for tests, `black`/`ruff` for formatting/linting. Document commands in README or a CONTRIBUTING file.

PR checklist for AI-generated changes
- Small, focused commit(s) with a clear message.
- A short `README` or `notebooks/` demo showing the new code works.
- At least one deterministic test in `tests/` validating the numerical step or a conserved quantity.

If you are uncertain
- Ask before making large structural changes (adding major language ecosystems, large CI, or re-licensing).
- If the numerical model's constants or physical interpretation are unclear, open an issue describing assumptions and the minimal tests you'd add.

Contact & housekeeping
- License: repository-level license is MIT (see top-level README text). When adding new files include short headers or references to the MIT license.
- After making changes, ping the maintainer with a brief summary and the relevant file links (e.g., `src/`, `notebooks/`, `tests/`).

---
If anything in these instructions is unclear or incomplete, leave a short issue or ask in the PR description so the maintainer can clarify.
