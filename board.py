def print_board(b):

    print("  0   1   2   3   4   5   6   7   8   9  ")
    print("-----------------------------------------")
    
    rowno = 0

    for row in b:
        rowno += 1
        
        line = "| "
        for element in row:
            line += str(element) if element != 0 else " "
            line += " | "
        
        print(line, rowno - 1)
        print("-----------------------------------------")
