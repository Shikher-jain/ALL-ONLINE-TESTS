# Maximum Alternating Sum Subarray

## Problem Statement

Given an array `A` of `n` positive integers, find the maximum sum of a contiguous subarray where the elements satisfy an **alternating sign pattern** when we compute their differences.

More formally, a subarray `A[i..j]` is **valid** if:
- For every position `k` where `i < k < j`, the differences satisfy: `(A[k] - A[k-1]) * (A[k+1] - A[k]) < 0`

This means the trend must alternate: if one difference is positive, the next must be negative, and vice versa.

### Example

For array `[1, 3, 2, 5, 1, 4]`:
- Subarray `[1, 3, 2]`: differences are `+2, -1` → alternating ✓
- Subarray `[1, 3, 2, 5]`: differences are `+2, -1, +3` → alternating ✓
- Subarray `[1, 3, 2, 5, 1]`: differences are `+2, -1, +3, -4` → alternating ✓
- Subarray `[1, 3, 2, 5, 1, 4]`: differences are `+2, -1, +3, -4, +3` → alternating ✓

The entire array forms a valid alternating pattern with sum = `1 + 3 + 2 + 5 + 1 + 4 = 16`.

However, if we had `[1, 3, 2, 5, 3, 4]` instead:
- Differences: `+2, -1, +3, -2, +1` → NOT alternating (last two are `-2, +1` but then we'd need the next to be negative)
- Valid subarrays: `[1,3,2,5]` (sum=11), `[2,5,3,4]` (sum=14), etc.

## Input Format

- First line: integer `n` (1 ≤ n ≤ 10^5)
- Second line: `n` space-separated integers `A[0], A[1], ..., A[n-1]` (1 ≤ A[i] ≤ 10^9)

## Output Format

A single integer: the maximum sum of any valid alternating subarray.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ A[i] ≤ 10^9
- Time Limit: 2 seconds
- Memory Limit: 256 MB

## Notes

- If no valid subarray exists (only single elements), return the maximum single element
- A subarray of length 1 is always valid
- A subarray of length 2 is always valid (no middle elements to check)
