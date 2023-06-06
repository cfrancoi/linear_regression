

import sys

from utils import utils

def main() -> int:
    wanted = input("Enter wanted milenage price: ")

    try:
        wanted = int(wanted)
    except ValueError: # TODO check and send error message
        return 1
    
    price = utils.estimate_price(0, 0, wanted) #TODO get th0 abd th1

    print(f"Estimated price: {price}")
    return 0

if __name__ == "__main__":
    sys.exit(main())