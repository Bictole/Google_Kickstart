import math

def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))

def solve(A):
    res = 0

    for i in range(1, A + 1):
        if A % i == 0:
            if i == rev(i):
                res += 1

    return res


if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        A = int(input())
        print("Case #{}:".format(t), solve(A))