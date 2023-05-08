def estimate_price(th0: float, th1: float, mileage: int) -> int:
    """
    Estimate the price of the product.
    :param th0: Theta0
    :param th1: Theta1 
    :return:    
    """
    return (th0 + (th1 * mileage))