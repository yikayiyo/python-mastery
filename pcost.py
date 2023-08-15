filename = 'Data/portfolio.dat'

def portfolio_cost(filename=filename):
  total = 0
  with open(filename, 'r') as f:
    for line in f:
      fields = line.split()
      try:
        total += int(fields[1]) * float(fields[2])
      except ValueError as e:
        print("Couldn't parse:", repr(line))
        print("Reason:", e)
  return total

if __name__ == '__main__':
  print(portfolio_cost('Data/portfolio3.dat'))