def match(a, b):
    """Where a,b are DNA bases (chars)"""
    # Yes I know this is slow because we must initalize dict each call
    # But it would be UGLY to have this in seq_sim()
    match = { 'A' : {'A' : 1,
                     'G': -0.1,
                     'C' : -0.1,
                     'T' : -0.15},
              'G' : {'A' : -0.1,
                     'G' : 1,
                     'C' : -0.15,
                     'T' : -0.1},
              'C' : {'A' : -0.1,
                     'G' : -0.15,
                     'C' : 1,
                     'T' : -0.1},
              'T' : {'A' : -0.15,
                     'G' : -0.1,
                     'C' : -0.1,
                     'T' : 1}
             }
    return match[a][b]

def seq_sim(x, y):
    """Where x,y are DNA sequences (strings)"""
    #TODO: Do backtracking. Perhaps use a 2D array of length-3-bitfields (up/left/diag)?
    x = " " + x
    y = " " + y

    # 1. Initialize table of size |X|x|Y|
    table = [[0 for j in range(len(y))] for i in range(len(x))]

    # 2. Populate first row/column
    for i in range(1, len(x)): # Populate first column
        table[i][0] = table[i-1][0] - 0.2

    for j in range(1, len(y)): # Populate first row
        table[0][j] = table[0][j-1] - 0.2

    # 3. Populate rest of table, one row at a time
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            up = table[i][j-1] - 0.2
            left = table[i-1][j] - 0.2
            diag = table[i-1][j-1] + match(x[i], y[j])
            table[i][j] = max(up, left, diag)

    return table


temp = seq_sim("GTGAAC", "AGCTAA")
for i in range(0, len(temp)):
    for j in range(0, len(temp[i])):
        print(temp[i][j], "\t", end="")
    print("")
