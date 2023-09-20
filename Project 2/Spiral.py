#  File: Spiral.py

#  Description: Creates a spiral of n x n dimension, where n is an odd number, and finds the sum of all the adjacent numbers of some number(s) in the spiral.

#  Student Name: Pratham Gujar

#  Student UT EID: psg635

#  Partner Name: Faye Inguito

#  Partner UT EID: fi829

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: August 29th, 2023 

#  Date Last Modified: September 8th, 2023
import sys
def make_square(x, y, size, grid):
  """Helper function to create a square at a particular position around a smaller square. 
  The starting position is at the top right corner where, for the i-th square, the starting value equals 1 + (2 * i)
  where 1 is the starting value of the spiral."""

  # Initializes the starting number for the square.  
  num = size**2
  
  # Four for loops contructing a square distinguished by the sides abcd.  
  for a in range(size - 1):
    grid[y][x] = num
    x -= 1
    num -= 1
  for b in range(size - 1):
    grid[y][x] = num
    y += 1
    num -= 1
  for c in range(size - 1):
    grid[y][x] = num
    x += 1
    num -= 1
  for d in range(size - 1):
    grid[y][x] = num
    y -= 1
    num -= 1
    
def create_spiral(n):
    """Creates an n x n spiral with the origin at the center."""

    spiral = [ [0 for i in range(n)] for j in range(n) ]

    # Defines the origin of the spiral and sets it equal to 1
    if len(spiral) != 0:
        origin = len(spiral) // 2
        spiral[origin][origin] = 1

        # Fill in the spiral
        for i in range(3, len(spiral) + 1, 2):
            x = origin + i // 2
            y = origin - i // 2
            make_square(x, y, i, spiral)
    
    return spiral

def sum_adj_num(spiral, n):
  """Sum the adjacent numbers around the number n in a spiral"""

  # Initializing x and y as -1 to handle the case when the spiral has length 0
  x = y = -1

  # Finds the position of the number n in spiral. If there is no such number, then return 0
  for i in range(len(spiral)):
    if n in spiral[i]:
      x = spiral[i].index(n)
      y = i
      break
    elif i == len(spiral) - 1:
      return 0

  # The series of if statements check all the possible adjacent places around n to see if they are within the range of the spiral.
  # If they exist, adds the number in that index into sum.  
  sum = 0
  if x < len(spiral) - 1:
    sum += spiral[y][x + 1]
  if (x < len(spiral) - 1) and (y > 0):
    sum += spiral[y - 1][x + 1]
  if y > 0:
    sum += spiral[y - 1][x]
  if (x > 0) and (y > 0):
    sum += spiral[y - 1][x - 1]
  if x > 0:
    sum += spiral[y][x - 1]
  if (x > 0) and (y < len(spiral) - 1):
    sum += spiral[y + 1][x - 1]
  if y < len(spiral) - 1:
    sum += spiral[y + 1][x]
  if (x < len(spiral) - 1) and (y < len(spiral) - 1):
    sum += spiral[y + 1][x + 1]
  
  return sum

def main():
    # Reads the data file and splits it by newline.
    data = sys.stdin.read()
    data_list = data.split("\n")

    # Creates spiral and removes the first line indicating the dimension of the spiral.
    spiral = create_spiral(int(data_list.pop(0)))

    # Sums adjacent numbers given that the line in data_list is a digit.
    for line in data_list:
       if line.strip().isdigit():
        print(sum_adj_num(spiral, int(line.strip())))

if __name__ == "__main__":
    main()
