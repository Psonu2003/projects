#  File: Work.py 

#  Description:  Determines the minimal amount of lines of code Vyasa needs to write in order to meet his goal based on his productivity factor

#  Student Name:  Pratham Gujar

#  Student UT EID:  psg635

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: October 1, 2023

#  Date Last Modified: October 2, 2023

import sys, time

# Input: int v which represents the number of lines of code that must be
#        written before the first cup of coffee, 
#        int k is the productivity factor, int n is the number of lines of code to write,
#        and int p is the number of coffees consumed
# Output: int n, the number of lines of code to write
def compute_lines(v, k, n = 0, p = 0):
  if v // (k**p) == 0:
    return n
  else:
    return compute_lines(v, k, n + v // (k**p), p + 1)

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
  v = 1
  while True:
    if compute_lines(v, k) >= n:
      return v
    v += 1

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  low = 0
  high = n

  while low <= high:
    v = (low + high) // 2

    n_prime = compute_lines(v, k)
    if n_prime < n:
      low = v + 1
    else:
      high = v - 1
  
  return low
    

  return n

# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

