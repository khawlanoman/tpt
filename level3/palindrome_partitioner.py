def py_palindrome_partitioner(s: str) -> int:
    n = len(s)

    if n <= 1:
        return 0

    dp = [0] * n

    for i in range(n):
        dp[i] = i

        for j in range(i + 1):
            sub = s[j:i + 1]

            if sub == sub[::-1]:
                if j == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[n - 1]
print(palindrome_partitioner("abc"))