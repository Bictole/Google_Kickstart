from cmath import pi


def solve(arr):
    R = arr[0]
    A = arr[1]
    B = arr[2]

    res = pi * (R**2)

    mult_a = True
    while R != 0:
        if mult_a:
            R = R * A
            res += pi * (R**2)
            mult_a = False
        else:
            R = R // B
            res += pi * (R**2)
            mult_a = True

    return res


if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        arr = list(map(int, input().split()))
        print("Case #{}:".format(t), solve(arr))