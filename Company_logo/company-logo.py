from collections import Counter

def company_logo(string_):
        return sorted(Counter(string_).most_common(), 
                     key = lambda x: (-x[1], x[0]))[:3]

if __name__ == '__main__':
    string_ = input()
    orded_s = company_logo(string_)
    print('\n'.join([letter_count[0]+ ' '+ str(letter_count[1]) for letter_count in orded_s]))