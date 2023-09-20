import sys
def print_square(magic_square):
  """Prints the magic square without the brackets and even spacing"""

  # Spaces out the numbers in the output according to the length of the largest number for better appearance.   
  space = len(str(len(magic_square)**2)) + 1

  for row in magic_square:
    r = ""
    for i in range(len(magic_square)):
      r += format(row[i], str(space))
    print(r)

def make_magic_square(n):
  """Creates a magic square of dimension n given that n is an odd integer"""

  square = [ [0 for i in range(n)] for j in range(n) ]
  dim = len(square)

  # Calculates the middle of the bottom row position.
  x = dim // 2
  y = dim - 1

  # Fills in the magic square from 1 to n^2 adhering to the three given rules.
  k = 0
  while k < n**2:
    k += 1

    # Checks if the current position is at the bottom right corner.
    if (x == dim - 1 and y == dim - 1):
      square[y][x] = k
      y -= 1
      continue

    # Checks if the current position is filled.  
    if square[y][x] != 0:
      x -= 1
      y -= 2


    square[y][x] = k

    # Increments the x and y positions but is kept bounded within the dimensions of the magic square. 
    x = (x + 1) % dim
    y = (y + 1) % dim

  return square


def check_square(magic_square):
  """Verifies if the argument is a magic square"""

  dim = len(magic_square)
  # s represents the representative sum to compare all the other sums to.
  s = sum(magic_square[0])
  result = False

  # Checks the sum of each row and compares it to the representative sum.  
  for row in range(1, dim):
    if s == sum(magic_square[row]):
      result = True
    else:
      return False

  # Compares the sum of each column to the representative sum.  
  for col in range(dim):
    temp = 0
    for row in magic_square:
      temp += row[col]
    if s == temp:
      result = True
    else:
      return False

  # Checks the diagonal sum of the magic square and compares to representative sum.  
  temp = 0
  for diag in range(dim):
    temp += magic_square[diag][diag]

  if s == temp:
      result = True
  else:
    return False

  #  Checks the antidiagonal sum of the magic square and compares to representative sum. 
  temp = 0
  for antidiag in range(dim - 1, -1, -1):
    temp += magic_square[antidiag][antidiag]

  if s == temp:
      result = True
  else:
    return False

  return result

def sum_adj_num(square, n):
  """Sum the adjacent numbers around the number n in a magic square"""
  dim = len(square)

  # Finds the position of the number n in magic square. If there is no such number, then return 0
  for i in range(dim):
    if n in square[i]:
      x = square[i].index(n)
      y = i
      break
    elif i == dim - 1:
      return 0

# The series of if statements check all the possible adjacent places around n to see if they are within the range of the magic square.
# If they exist, adds the number in that index into sum. 
  sum = 0
  if x < dim - 1:
    sum += square[y][x + 1]
  if (x < dim - 1) and (y > 0):
    sum += square[y - 1][x + 1]
  if y > 0:
    sum += square[y - 1][x]
  if (x > 0) and (y > 0):
    sum += square[y - 1][x - 1]
  if x > 0:
    sum += square[y][x - 1]
  if (x > 0) and (y < dim - 1):
    sum += square[y + 1][x - 1]
  if y < dim - 1:
    sum += square[y + 1][x]
  if (x < dim - 1) and (y < dim - 1):
    sum += square[y + 1][x + 1]

  return sum

def main():
    # Reads the data file and splits it by newline.
    data = sys.stdin.read()
    data_list = data.split("\n")

    # Creates magic square and removes the first line indicating the dimension of the magic square.
    magic_square = make_magic_square(int(data_list.pop(0)))

    # Sums adjacent numbers given that the line in data_list is a digit.
    for line in data_list:
       if line.strip().isdigit():
        print(sum_adj_num(magic_square, int(line.strip())))

if __name__ == "__main__":
    main()
