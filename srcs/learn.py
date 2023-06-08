
import sys
import csv
import matplotlib.pyplot as plt
from statistics import mean, pstdev, quantiles

from utils import utils

learningRate = float(0.005)
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

def get_cost(X, Y, th0, th1, M) -> float:
    value= 0
    for i in range(M):
        value += float(utils.estimate_price(th0, th1, X[i]) - Y[i])**2
    
    cost = (1/2*M) * (value)

    return cost

    


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
    tmp0 = float(0)
    tmp1 = float(0)
    for i in range(0, M):
        value = utils.estimate_price(th0, th1, X[i])
        tmp = float(value - Y[i])
        tmp0 += tmp
        tmp1 += float(tmp * X[i])
        # print("=== {th0} {th1} {value} X={x} Y={y} ===".format(th0=tmp0, th1=tmp1, value=value, x=X[i], y=Y[i]))
        

    tmp0 = float(learningRate * tmp0 * float(1/M) )
    tmp1 = float(learningRate * tmp1 * float(1/M))

    # tmp1 = 0

    print("===  LEARN: {th0} {th1} ===".format(th0=tmp0, th1=tmp1))
    

    return [tmp0, tmp1]

def get_new_theta(X, Y, M, th0, th1, rep):
    cost = []

    for _ in range(0, rep):
        [tmp0, tmp1] = gradient_descent(X, Y, M, th0, th1)
        th0 = th0 - tmp0
        th1 = th1 - tmp1
        cost.append(get_cost(X, Y, th0, th1, M))
        print("last theta: {th0} {th1} {cost}".format(th0=th0, th1=th1, cost=cost[-1]))
    
    return [th0, th1, cost, theta0, theta1]

def normalize(lst):
    new_lst = []

    lst_mean = mean(lst)
    o = pstdev(lst)

    [q1, q2, q3] = quantiles(lst)

    for value in lst:
        # new_lst.append((value - max(lst)) / (max(lst) - min(lst)))
        new_lst.append((value - lst_mean) / (o))
        # new_lst.append((value - lst_mean) / (q3 - q1))

    return new_lst


def main() -> int:
    [X, Y] = get_data()

    M = len(X)

    x_train = normalize(X)
    y_train = normalize(Y)

    [th0, th1] = get_last_theta()

    print(M)
    print("last theta: {th0} {th1}".format(th0=th0, th1=th1))

    [new_th0, new_th1, cost] = get_new_theta(x_train, y_train, M, th0, th1, 10)

    
    print("new theta: {th0} {th1}".format(th0=new_th0, th1=new_th1))
    
    figure, axis = plt.subplots(1, 3)

    line_x = [min(X), max(X)]
    line_y = [(new_th1 * i) + new_th0 for i in line_x]
    axis[0].plot(line_x, line_y, 'b')
    axis[0].plot(X, Y, 'ro')

    axis[1].plot(cost)
    plt.show()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
