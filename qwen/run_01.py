# Qwen Run 1: Greedy Approach (Expected to Fail)
# This solution greedily extends subarrays without properly tracking state

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    if n <= 2:
        print(sum(A[:n]))
        return
    
    max_sum = max(A)
    current_sum = A[0]
    
    for i in range(1, n):
        if i < 2:
            current_sum += A[i]
        else:
            diff1 = A[i-1] - A[i-2]
            diff2 = A[i] - A[i-1]
            
            # Greedy: if alternating, just keep adding
            if diff1 * diff2 < 0:
                current_sum += A[i]
            else:
                # Start fresh - but this loses optimal solutions
                # that include previous elements with different starting points
                max_sum = max(max_sum, current_sum)
                current_sum = A[i]
    
    max_sum = max(max_sum, current_sum)
    print(max_sum)

solve()
