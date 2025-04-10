def calc_ear(nominal_rate, compounding_periods):
    """
    The Effective Annual Rate represents the actual growth. 
    It's the percentage increase over the original principal.
    """
    return (1 + nominal_rate/compounding_periods)**(compounding_periods) - 1