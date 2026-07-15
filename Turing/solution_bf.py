def solve_brute_force():
    """
    Brute force O(n^2) solution for testing purposes.
    Checks all possible subarrays and validates each one.
    """
    n = int(input())
    A = list(map(int, input().split()))
    
    max_sum = max(A)  # Single element is always valid
    
    # Check all subarrays
    for i in range(n):
        for j in range(i+1, n+1):
            subarray = A[i:j]
            length = len(subarray)
            
            # Check if subarray is valid
            valid = True
            if length >= 3:
                for k in range(1, length-1):
                    diff1 = subarray[k] - subarray[k-1]
                    diff2 = subarray[k+1] - subarray[k]
                    # Check if differences don't alternate
                    if diff1 * diff2 >= 0:  # Same sign or contains zero
                        valid = False
                        break
            
            if valid:
                current_sum = sum(subarray)
                max_sum = max(max_sum, current_sum)
    
    print(max_sum)

solve_brute_force()
