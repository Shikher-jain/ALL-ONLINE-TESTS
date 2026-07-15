# Maximum Alternating Sum Subarray - Problem Submission

## Overview

This is an original competitive programming problem designed for **Codeforces Div2/Low Div1** level difficulty.

## Problem Summary

Given an array of positive integers, find the maximum sum of a contiguous subarray where adjacent differences form an **alternating pattern** (positive-negative-positive or negative-positive-negative).

## Files Included

### Core Problem Files
- `problem.md` - Complete problem statement with examples and constraints
- `solution.py` - Optimal O(n) dynamic programming solution
- `solution.md` - Detailed explanation of the algorithm and approach

### Testing Files
- `test_cases/` - 5 comprehensive test cases covering:
  - Normal alternating patterns (Test 1)
  - Single element edge case (Test 2)
  - Two-element case (Test 3)
  - Strictly increasing array (Test 4)
  - Complex mixed pattern (Test 5)
- `solution_bf.py` - Brute force O(n²) solution for validation
- `generator.py` - Test case generator for additional validation

### Development Documentation
- `idea.md` - How the problem idea was conceived and refined
- `requirements.json` - Time and memory constraints

### Qwen Model Attempts
- `qwen/run_01.py` - Failed greedy approach
- `qwen/run_02.py` - Failed incorrect pattern matching
- `qwen/run_03.py` - Failed incomplete DP
- `qwen/conversations.md` - Links to Qwen chat conversations

## Problem Characteristics

### Originality
This problem is **not a known variation**. The specific alternating difference pattern requirement is novel and not found in standard competitive programming problem databases.

### Difficulty
- Requires understanding of dynamic programming with state tracking
- Multiple solution approaches possible but non-trivial
- Edge cases require careful implementation
- Suitable for Div2 contests or easy Div1 problems

### Algorithmic Concepts
- Dynamic Programming
- State management
- Greedy/DP hybrid thinking
- Pattern recognition

## How to Use

### Run the optimal solution:
```bash
python solution.py < test_cases/1.in
```

### Validate with brute force:
```bash
python solution_bf.py < test_cases/1.in
```

### Run all test cases:
```bash
for i in {1..5}; do
    echo "Test case $i:"
    python solution.py < test_cases/$i.in
    echo "Expected: $(cat test_cases/$i.out)"
    echo "---"
done
```

## Time & Space Analysis

| Metric | Value |
|--------|-------|
| Time Complexity | O(n) |
| Space Complexity | O(n) - can be optimized to O(1) |
| Time Limit | 2 seconds |
| Memory Limit | 256 MB |

## Author Notes

The problem was carefully designed to:
1. Be original and not found through search engine checks
2. Require genuine algorithmic thinking
3. Have multiple "plausible but wrong" solutions that Qwen attempts
4. Be implementable in various languages with similar complexity
5. Have clear, unambiguous problem statement

All test cases have been verified to produce correct results.
