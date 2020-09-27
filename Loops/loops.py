def n_smaller(n):
  return [i*i for i in range(n)]

if __name__ == '__main__':
  n = int(input())
  print(*n_smaller(n), sep='\n')


# It's also possible to direct answer print(*[i*i for i in range(n)], sep='')