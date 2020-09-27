def consecutive_values(n):
  return range(1,n+1)

if __name__ == '__main__':
    n = int(input())
    print(*consecutive_values(n), sep='')


# It's also possible to direct answer print(*range(1,n+1), sep='')