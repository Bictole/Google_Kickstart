def solve(arr):
    res = 0
    return res


if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        arr = list(map(int, input().split()))
        print("Case #{}:".format(t), solve(arr))