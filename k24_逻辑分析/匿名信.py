def main():
    newspaper = set(''.join(sorted(x)) for x in input().split())
    anonymousLetter = set(''.join(sorted(x)) for x in input().split())
    if anonymousLetter <= newspaper:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
