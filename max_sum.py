# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

def maxSubArray(A):
  if not A:
      return 0

  curSum = maxSum = A[0]
  for num in A[1:]:
    curSum = max(num, curSum + num)
    maxSum = max(maxSum, curSum)

  return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,3]))
