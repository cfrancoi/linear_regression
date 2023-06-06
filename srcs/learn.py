
import sys
import csv
import matplotlib.pyplot as plt

from utils import utils

learningReate: float = 1e-11
THETA_FILE = "theta.csv"

#move to utils
def get_last_theta() -> [float, float]:
    th0, th1 = 0, 0
    try:
        with open(THETA_FILE, newline='') as csvfile:
                fieldnames = ['th0', 'th1']
                data = csv.DictReader(csvfile, fieldnames=fieldnames)
                x = 0
                for field in data:
                    print(field['km'], field['price'])
                    if (x != 0): #TODO check a better way
                        th0 = float(field['th0'])
                        th1 = float(field['th1'])
                    x += 1
    finally:
        return [th0, th1]


def get_data() -> [[], []]:
    X, Y = [], []
    with open(sys.argv[1], newline='') as csvfile:
            fieldnames = ['km', 'price']
            data = csv.DictReader(csvfile, fieldnames=fieldnames)
            x = 0
            for field in data:
                print(field['km'], field['price'])
                if (x != 0): #TODO check a better way
                    X.append(float(field['km']))
                    Y.append(float(field['price']))
                x += 1
                
    return [X, Y]

def gradient_descent(X, Y, M, th0, th1):
    tmp0, tmp1 = 0, 0
    for i in range(0, M - 1):
        tmp0 += utils.estimate_price(th0, th1, X[i]) - Y[i]
        tmp1 += (utils.estimate_price(th0, th1, X[i]) - Y[i]) * X[i]

    tmp0 = tmp0 * learningReate * float(1/M)
    tmp1 = tmp1 * learningReate * float(1/M)

    return [tmp0, tmp1]

def get_new_theta(X, Y, M, th0, th1, rep):
    for i in range(0, rep - 1):
        [tmp0, tmp1] = gradient_descent(X, Y, M, th0, th1)
        th0 = th0 - tmp0;
        th1 = th1 - tmp1;
        # print("last theta: {th0} {th1}".format(th0=th0, th1=th1))
    
    return [th0, th1]

def main() -> int:
    [X, Y] = get_data()
    M = len(X)

    [th0, th1] = get_last_theta()

    print(M)
    print("last theta: {th0} {th1}".format(th0=th0, th1=th1))

    [new_th0, new_th1] = get_new_theta(X, Y, M, th0, th1, 100000)

    
    print("new theta: {th0} {th1}".format(th0=new_th0, th1=new_th1))
    print(utils.estimate_price(new_th0, new_th1, 60949))
    
    plt.plot(X, Y, 'ro')
    plt.show()
        
    return 0


if __name__ == "__main__":
    sys.exit(main())