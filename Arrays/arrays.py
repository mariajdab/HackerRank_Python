import numpy 

def arrays(arr):
    arr_ = numpy.array(arr, float)
    return arr_[::-1]

if __name__ == '__main__':
  arr = input().strip().split(' ')  #code line gives for HackerRank
  print(arrays(arr))  #code line gives for HackerRank
