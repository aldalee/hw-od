def guess(questions, answers):
    resList = []
    m, n = len(questions), len(answers)
    for i in range(m):
        questions_str = "".join(sorted(set(questions[i])))
        found = False
        for j in range(n):
            answers_str = "".join(sorted(set(answers[j])))
            if answers_str == questions_str:
                resList.append(answers[j])
                found = True
        if not found:
            resList.append("not found")
    return resList


def main():
    questions, answers = input().split(","), input().split(",")
    print(",".join(guess(questions, answers)))


if __name__ == '__main__':
    main()
