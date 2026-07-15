def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    if n == 1:
        print(A[0])
        return
    
    if n == 2:
        print(A[0] + A[1])
        return
    
    max_sum = max(A)  # At least one element
    
    # dp[i][j] = (max_sum, current_sum, valid_length)
    # j=0: last difference was positive
    # j=1: last difference was negative
    
    # We track: for each position and each state, what's the max sum we can get
    # and the current sum if we're building
    
    dp = [[0, 0] for _ in range(n)]  # dp[i][state] = (max_sum_ending_at_i_with_state)
    
    # Initialize: each position can start a new subarray
    # dp[0][0] and dp[0][1] don't exist for position 0
    
    # For position 1:
    diff = A[1] - A[0]
    if diff > 0:
        # First difference is positive, we can extend
        dp[1][0] = A[0] + A[1]  # Last diff was positive
    else:
        # First difference is negative
        dp[1][1] = A[0] + A[1]  # Last diff was negative
    
    max_sum = max(max_sum, dp[1][0], dp[1][1])
    
    # Fill DP table
    for i in range(2, n):
        diff_curr = A[i] - A[i-1]
        diff_prev = A[i-1] - A[i-2]
        
        # Determine if differences alternate
        # If prev > 0 and curr < 0, or prev < 0 and curr > 0, they alternate
        alternates = diff_prev * diff_curr < 0
        
        # Case 1: Start fresh at position i-1
        new_start_pos_i = A[i-1] + A[i]
        
        # Case 2: Extend from previous valid states
        if alternates:
            # We can extend
            # If last diff was positive (dp[i-1][0]), current must be negative
            if diff_curr < 0:
                if dp[i-1][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i-1][0] + A[i])
            # If last diff was negative (dp[i-1][1]), current must be positive
            if diff_curr > 0:
                if dp[i-1][1] > 0:
                    dp[i][0] = max(dp[i][0], dp[i-1][1] + A[i])
        
        # Always can consider starting a new subarray at i-1
        if diff_curr > 0:
            dp[i][0] = max(dp[i][0], new_start_pos_i)
        elif diff_curr < 0:
            dp[i][1] = max(dp[i][1], new_start_pos_i)
        
        max_sum = max(max_sum, dp[i][0], dp[i][1])
    
    print(max_sum)

solve()
