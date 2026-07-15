# Qwen Run 2: Incorrect Pattern Recognition (Expected to Fail)
# This solution misunderstands the alternating pattern requirement

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    if n == 1:
        print(A[0])
        return
    
    max_sum = max(A)
    
    # Incorrect interpretation: thinks it needs to alternate between 
    # picking indices, not checking differences
    for i in range(n):
        current_sum = A[i]
        for j in range(i+1, n):
            # Wrong logic: alternating indices
            if (j - i) % 2 == 1:
                current_sum += A[j]
            max_sum = max(max_sum, current_sum)
    
    print(max_sum)

solve()
