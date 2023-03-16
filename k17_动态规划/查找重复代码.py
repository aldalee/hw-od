def LongestCommonSubsequence(s1, s2):
    m, n = len(s1), len(s2)
    maxLength, ans = 0, ""
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > maxLength:
                maxLength = dp[i][j]
                ans = s1[i - dp[i][j]: i]
    return ans


def main():
    s1, s2 = input().strip(), input().strip()
    print(LongestCommonSubsequence(s1, s2))


if __name__ == '__main__':
    main()
