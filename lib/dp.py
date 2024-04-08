def dynamic_plan(dp, S):
    for i in range(len(S)):
        dp[i + 1] += max(dp[i], dp[i] + S[i])
    return dp
