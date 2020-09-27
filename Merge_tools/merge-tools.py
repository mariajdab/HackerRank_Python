def merge_the_tools(S, k):
  len_S = len(S)
  subS_k_ord = [''.join({}.fromkeys(S[i:i+k])) for i in range(0,len_S,k)]  
  return subS_k_ord

if __name__ == '__main__':
  string, k = input(), int(input())
  print(*merge_the_tools(string, k), sep='\n')


""" In this code is used python 3.7 which standard says that the 
Dictionary order is guaranteed to be insertion order, therefore, 
fromkeys doesn't change the order just remove the duplicates."""