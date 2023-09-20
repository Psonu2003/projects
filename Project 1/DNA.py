import sys
def seqFinder(DNA1, DNA2, seq = None):
  if seq == None:
    seq = DNA1[0]
  if seq not in DNA2:
    return seq[0:len(seq)-1]
  elif DNA1 == "":
    return seq
  else:
    return seqFinder(DNA1[1:], DNA2, seq + DNA1[1:2])

def main():
    line = sys.stdin.readline()
    line = line.strip()

    numPairs = line
    dnaLST = []

    for i in range(int(numPairs)):
       dnaLST.append((sys.stdin.readline().strip().upper(), sys.stdin.readline().strip().upper()))

    for pair in dnaLST:
      print()
      DNA1 = max(pair[0], pair[1])
      DNA2 = min(pair[0], pair[1])
      temp = [""]

      while len(DNA1) > 0:
        seq = seqFinder(DNA1, DNA2)
        if len(seq) > len(temp[0]):
          temp.clear()
          temp.append(seq)
        elif len(seq) == len(temp[0]):
          temp.append(seq)
        DNA1 = DNA1[1:]
      
      temp.sort()
      if "" in temp:
        print("No Common Sequence Found")
      else:
        for s in temp:
          print(s)
      

if __name__ == "__main__":
  main()