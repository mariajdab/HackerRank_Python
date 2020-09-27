from collections import Counter

def word_or(words, num_):
    # dicts on version > python 3.6 the order is guaranteed to be insertion order
    return(Counter(words).values())

if __name__ == '__main__':
    num_ = int(input())
    words = [input() for _ in range(num_)]
    result = word_or(words, num_)
    print(len(result))
    print(*result, sep=' ')


 