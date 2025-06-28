# Day 16 – Climbing Stairs (Dynamic Programming)
## 📘 Overview
Implemented a solution to the classic "Climbing Stairs" problem using dynamic programming. The problem asks: In how many distinct ways can you climb to the top of a staircase with n steps, if you can take 1 or 2 steps at a time?

---
## 🧠 What I Learned
- Used bottom-up dynamic programming to avoid redundant calculations.

- Built the solution iteratively using a list to store intermediate results.

- Improved performance over recursive or naive approaches.
---
## 🧪 Sample Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        x = [1, 1]
        for i in range(1, n):
            x.append(x[i-1] + x[i])
        return x[-1]
```