from typing import List
from collections import defaultdict


def Reorder(arr: List[str]):
    for i in range(len(arr)):
        arr[i] = "".join(sorted(arr[i]))
    count = defaultdict(int)
    for i in arr:
        count[i] += 1
    arr.sort(key=lambda x: (-count[x], len(x), [ord(char) for char in x]))
    return " ".join(map(str, arr))


if __name__ == '__main__':
    print(Reorder(input().split()))
