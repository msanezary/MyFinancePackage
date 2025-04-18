# MyFinance

> **A beginner‑friendly Python toolkit for hands‑on financial maths**

---

## Key Features

| Module | What it does | Quick example |
|--------|--------------|---------------|
| **`ear.py`** | Convert nominal ↔ effective annual rate | `calc_ear(0.05, 12)  # 5% nominal, monthly compounding` |
| **`mc_european_call.py`** | Monte‑Carlo pricing for a European call option | `mc_european_call(S0=100, K=95, r=0.03, sigma=0.2, T=1, n_sims=50_000)` |
| **`pfr.py`** | Compute weighted portfolio returns | `portfolio_return(returns, weights)` |
| **`ruin.py`** | Simulate portfolio paths & ruin probability | `estimate_portfolio_ruin(initial=10_000, ... )` |

---

## Installation

```bash
# 1. Clone the repo (or download the zip)
git clone https://github.com/your‑user/myfinance.git
cd myfinance

# 2. Install the core library in editable mode
pip install -e .

# 3. (Optional) extras
pip install -e .[notebook]   # Jupyter & plotting stack
pip install -e .[dev]        # linting, tests, docs
```

> **Note for Windows & Python 3.13 users** – NumPy wheels are not yet available. Either use Python 3.11/3.12 or turn on Win‑Long‑Paths before installing.

---

## Quick‑start

```python
import numpy as np
from myfinance import calc_ear, mc_european_call

# Effective annual rate of 5% nominal, monthly compounding
print(calc_ear(0.05, 12))

# Price a 1‑year at‑the‑money call via Monte Carlo
price = mc_european_call(S0=100, K=100, r=0.025, sigma=0.18, T=1, n_sims=100_000)
print(f"Call price ≈ {price:.2f} USD")
```

---

## Project layout (monorepo)

```text
myfinance/               ← importable Python package
│  ├─ __init__.py
│  ├─ ear.py
│  ├─ mc_european_call.py
│  ├─ pfr.py
│  └─ ruin.py
│
├─ notebooks/            ← Jupyter notebooks
│  ├─ 00_Intro_To_Financial_Python.ipynb
│  └─ 01_Gambler's_Ruin.ipynb
│
├─ Weekly Plan.md        ← 10‑week brain‑teaser roadmap
├─ pyproject.toml        ← build & dependency config
└─ README.md             ← you are here
```

---

## Contributing

1. Fork ➜ create feature branch (`git checkout -b feat/my‑feature`)
2. Run `pre‑commit install` to enable auto‑formatting.
3. Add / update tests.
4. Open a PR – we’ll review ASAP!

---

## License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.

---

## Author
Mohammed Said Anezary  ·  [LinkedIn](https://www.linkedin.com/in/msanezary)  ·  [Email](mailto:msanezary@gmail.com)

---

