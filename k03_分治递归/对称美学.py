def find(n, k):
    if n == 1:
        return 'R'
    if n == 2:
        return 'B' if k == 0 else 'R'
    half = 1 << (n - 2)
    if k >= half:
        return find(n - 1, k - half)
    else:
        return 'R' if find(n - 1, k) == 'B' else 'B'


def main():
    T = int(input())
    for i in range(T):
        n, k = map(int, input().split(" "))
        if find(n, k) == 'R':
            print("red")
        else:
            print('blue')


if __name__ == '__main__':
    main()
