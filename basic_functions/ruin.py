def simulate_portfolio(initial, n_steps, returns='default', mu=None, sigma=None):
    """
    Simulates the portfolio value over time using either provided returns or generated ones.

    Parameters:
    - initial: float, initial portfolio value
    - n_steps: int, number of time steps (e.g., days)
    - returns: list/array of returns or 'default'
    - mu: float, mean daily return (used only if returns not provided)
    - sigma: float, standard deviation of returns (used only if returns not provided)

    Returns:
    - list of portfolio values at each time step
    """
    import numpy as np

    if isinstance(returns, (list, np.ndarray)) and (mu is not None or sigma is not None):
        raise ValueError("Provide either 'returns' OR 'mu' and 'sigma', not both.")

    if not isinstance(returns, (list, np.ndarray)) and (mu is None or sigma is None):
        raise ValueError("If 'returns' is not provided, you must specify both 'mu' and 'sigma'.")

    v = [initial]

    if isinstance(returns, (list, np.ndarray)):
        used_returns = np.random.choice(returns, size=n_steps, replace=True)
    else:
        used_returns = np.random.normal(mu, sigma, n_steps)

    for r in used_returns:
        v.append(v[-1] * (1 + r))

    return v


def estimate_portfolio_ruin(initial, n_steps, n_sims, threshold, returns='default', mu=None, sigma=None):
    """
    Estimates the probability of portfolio ruin using Monte Carlo simulation.

    Parameters:
    - initial: float, initial portfolio value
    - n_steps: int, number of time steps (e.g., days)
    - n_sims: int, number of Monte Carlo simulations
    - threshold: float, ruin threshold as a fraction of the initial value
    - returns: list/array of returns or 'default'
    - mu: float, mean daily return (used only if returns not provided)
    - sigma: float, standard deviation of returns (used only if returns not provided)

    Returns:
    - proba_ruin: float, estimated probability of ruin
    - paths: list of lists, simulated portfolio paths
    """
    import numpy as np

    if isinstance(returns, (list, np.ndarray)) and (mu is not None or sigma is not None):
        raise ValueError("Provide either 'returns' OR 'mu' and 'sigma', not both.")
    if not isinstance(returns, (list, np.ndarray)) and (mu is None or sigma is None):
        raise ValueError("If 'returns' is not provided, you must specify both 'mu' and 'sigma'.")

    ruin = threshold * initial
    c = 0
    paths = []

    for _ in range(n_sims):
        v = simulate_portfolio(initial, n_steps=n_steps, returns=returns, mu=mu, sigma=sigma)
        paths.append(v)
        if np.any(np.array(v) < ruin):
            c += 1

    proba_ruin = c / n_sims
    return proba_ruin, paths


