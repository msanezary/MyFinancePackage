def portfolio_return(returns, weights):
    """
    The function compute the weighted average return of a protfolio, where each asset's return is multiplied by its portfolio weight.
    """
    import numpy as np

    return np.dot(returns, weights/np.sum(weights))