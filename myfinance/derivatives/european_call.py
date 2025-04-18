def mc_european_call(S0, K, r, sigma, T, n_sims):
    """
    A function to estimate the price of a European call using Monte Carlo simulation
    
    S0 : the price of the asset now.
    K : the strike.
    r : the return.
    sigma : the volatility.
    T : number of years.
    n_sims : number of simulations
    """
    import numpy as np

    Z = np.random.normal(0, 1, n_sims)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(ST - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)