# Qwen Run 3: Incomplete DP (Expected to Fail)
# This solution attempts DP but doesn't properly handle all state transitions

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    if n <= 2:
        print(sum(A[:n]))
        return
    
    # Incomplete DP - doesn't track state properly
    dp = [0] * n
    dp[0] = A[0]
    dp[1] = A[0] + A[1]
    
    max_sum = max(dp[0], dp[1])
    
    for i in range(2, n):
        diff = A[i] - A[i-1]
        
        # Only checks previous position, misses complex state tracking
        if diff != 0:  # Wrong condition
            dp[i] = dp[i-1] + A[i]
        else:
            dp[i] = A[i]
        
        # Also doesn't consider starting fresh or proper continuation
        max_sum = max(max_sum, dp[i])
    
    print(max_sum)

solve()
