# Test Case Generator

import random

def generate_test_cases():
    """Generate additional test cases for validation."""
    
    # Test case 1: Random array
    n = random.randint(10, 100)
    arr = [random.randint(1, 1000) for _ in range(n)]
    print(f"Random test ({n} elements):", arr)
    
    # Test case 2: All alternating
    arr = []
    for i in range(20):
        if i % 2 == 0:
            arr.append(i + 1)
        else:
            arr.append(100 - i)
    print(f"Alternating pattern test:", arr)
    
    # Test case 3: Edge case - large numbers
    arr = [10**9, 1, 10**9, 1, 10**9]
    print(f"Large numbers test:", arr)

if __name__ == "__main__":
    generate_test_cases()
