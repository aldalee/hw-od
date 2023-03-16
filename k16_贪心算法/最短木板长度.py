import heapq


def GetShortestLength(woods, m):
    heap = []
    for wood in woods:
        heapq.heappush(heap, wood)

    for i in range(m):
        curr_wood = heapq.heappop(heap)
        curr_wood += 1
        heapq.heappush(heap, curr_wood)
    return heapq.heappop(heap)


def main():
    n, m = map(int, input().split(" "))
    woods = list(map(int, input().split(" ")))
    print(GetShortestLength(woods, m))


if __name__ == '__main__':
    main()
