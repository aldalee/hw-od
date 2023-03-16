def Res(words):
    res = []
    word = ""
    for _, c in enumerate(words):
        if c.isalpha():
            word += c
        else:
            res.append(word[::-1])
            res.append(c)
            word = ""
    res.append(word[::-1])
    return "".join(res)


def main():
    words = input()
    print(Res(words))


if __name__ == '__main__':
    main()
