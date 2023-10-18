import sys

def sum_squares(n, numbers, sum = 0):
  """Recursively finds the sum of all the squares from a string input of numbers"""

  # Base case to deal with final number
  if n == 1:
    return sum + int(numbers[: len(numbers)])**2
  
  # Handles negative numbers
  elif numbers[0] == "-":
    return sum_squares(n - 1, numbers[numbers.find(" ") + 1 :], sum)
  
  # Recursive case to sum the next square
  else:
    return sum_squares(n - 1, numbers[numbers.find(" ") + 1 :], sum + int(numbers[: numbers.find(" ")])**2)
  
def test_cases(n, test_cases_sums = ""):
  """Recursively takes in inputs and returns the sums for each test case as a string seperated by a space"""

  # Base case to return the sums
  if n == 0:
    return test_cases_sums.strip()
  
  # Recursive case to take all test cases and store each respective sum
  else:
    X = int(sys.stdin.readline().strip())
    Yn = sys.stdin.readline().strip()
    test_cases_sums += str(sum_squares(X, Yn)) + " "
    return test_cases(n - 1, test_cases_sums)
  
def print_test_cases(n, test_cases_sums):
  """Recursively prints the sums of each test case"""

  # Base case to print the final test case's sum
  if n == 1:
    print(test_cases_sums)

  # Recursive case to print all n - 1 test cases sums
  else:
    print(test_cases_sums[: test_cases_sums.find(" ")])
    return print_test_cases(n - 1, test_cases_sums[test_cases_sums.find(" ") + 1 :])
  
def main():
  # Takes in the number of test cases
  N = int(sys.stdin.readline().strip())

  sums = test_cases(N)
  print_test_cases(N, sums)

if __name__ == "__main__":
  main()
