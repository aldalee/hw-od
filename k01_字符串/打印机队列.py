import heapq


def PrintProcess(orders):
    f_id = 0
    printers = [[] for _ in range(5)]
    for i, order in enumerate(orders):
        if order[0] == "IN":
            p, rank = map(int, order[1:])
            f_id += 1
            heapq.heappush(printers[p - 1], (-rank, f_id))
        elif order[0] == "OUT":
            p = int(order[1])
            if printers[p - 1]:
                print(heapq.heappop(printers[p - 1])[1])
            else:
                print("NULL")


def main():
    n = int(input())
    orders = [input().split(" ") for _ in range(n)]
    PrintProcess(orders)


if __name__ == '__main__':
    main()
