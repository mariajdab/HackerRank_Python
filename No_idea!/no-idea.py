from collections import Counter

def no_idea_(n, a, b):
  cont = Counter(n)
  a_in_keys = cont.keys() & set(a)
  b_in_keys = cont.keys() & set(b)
  num_a_in_n = [cont[i] for i in a_in_keys]
  num_b_in_n = [cont[i] for i in b_in_keys]
  return sum(num_a_in_n) - sum(num_b_in_n)

if __name__ == '__main__':
    _, n, a, b  = ((input().split(' ')) for _ in range(4))
    print(no_idea_(n, a, b))

""" In this code is created a Counter dict, next the intersection with the 
    set 'a'&keys and the set 'b'&keys of the dict. Now the keys that really 
    matters is known, therefore, the values that are the count of each letter 
    in the string."""





