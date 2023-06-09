

import sys

from utils.utils import estimate_price
from learn import get_last_theta

def main() -> int:
    wanted = input("Enter wanted milenage price: ")

    try:
        wanted = int(wanted)
    except ValueError: # TODO check and send error message
        return 1

    [th0, th1] = get_last_theta()
    
    price = estimate_price(th0, th1, wanted) #TODO get th0 abd th1

    print(f"Estimated price: {price}")
    return 0

if __name__ == "__main__":
    sys.exit(main())