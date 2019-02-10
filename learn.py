# @author: Matthew Drew
# @github: https://github.com/moshulu
#
# learn.py
# @description: A simple machine learning algorithm, using the perceptron algorithm.
# © Matthew Drew 2019, All Rights Reserved.

# initialize variables
n = 1
w = (1,0,0)
input = ((1,1,1),(1,1,-1),(1,0,-1),(1,-1,-1),(1,-1,1),(1,0,1))
desired = (1,1,1,0,0,0)


def dotProduct(w, input):
    w0 = w[0]
    w1 = w[1]
    w2 = w[2]
    x0 = input[0]
    x1 = input[1]
    x2 = input[2]
    b = w0 * x0

    ans = b + (w1*x1) + (w2*x2)
    return ans

def change_weight(w, input, d, ans):
    #print(w[0], " + " , n , " * (" , d , " - " , ans , ") * " , input[0])
    w0 = w[0] + n * (d - ans) * input[0]
    w1 = w[1] + n * (d - ans) * input[1]
    w2 = w[2] + n * (d - ans) * input[2]
    return (w0,w1,w2)

for i in range(0,3):
    count = 0
    for x in input:
        print("\n")
        print("x: ", x)
        print("w: ", w)
        print("d: ", desired[count])
        ans = dotProduct(w, x)
        print("actual: ", ans)
        if(ans < 0):
            ans = 0
            if(ans == desired[count]):
                count = count + 1
                print("No")
                continue
            else:
                print("Yes")
                w = change_weight(w, x, desired[count], ans)
        else:
            ans = 1
            if(ans == desired[count]):
                count = count + 1
                print("No")
                continue
            else:
                print("Yes")
                w = change_weight(w, x, desired[count], ans)

        count = count + 1

    print("======================")
