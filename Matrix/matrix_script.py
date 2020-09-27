import re

rows, col = map(int, input().split())
matrix = [input() for _ in range(rows)]
read_columns = ''.join([row[i] for i in range(col) for row in matrix])

print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', read_columns))
