import math

P, O, E = 'X', 'O', ' '

W = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def print_board(b):
    for i in range(0,9,3):
        print(f"{b[i]} | {b[i+1]} | {b[i+2]}")
    print()

def eval(b):
    for x,y,z in W:
        if b[x]==b[y]==b[z]!=E:
            return 10 if b[x]==P else -10
    return 0

def moves_left(b): return E in b

def minimax(b, is_max):
    s = eval(b)
    if s or not moves_left(b): return s

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i]==E:
                b[i]=P
                best = max(best, minimax(b, False))
                b[i]=E
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i]==E:
                b[i]=O
                best = min(best, minimax(b, True))
                b[i]=E
        return best

def best_move(b):
    m, best = -1, -math.inf
    for i in range(9):
        if b[i]==E:
            b[i]=P
            v = minimax(b, False)
            b[i]=E
            if v>best: best, m = v, i
    return m

def winner(b):
    for x,y,z in W:
        if b[x]==b[y]==b[z]!=E:
            return b[x]
    return None

b = [E]*9

while True:
    print_board(b)

    p = int(input("Enter (1-9): ")) - 1
    if b[p]!=E: continue
    b[p]=O

    if winner(b)==O:
        print_board(b); print("You win"); break
    if not moves_left(b):
        print_board(b); print("Draw"); break

    b[best_move(b)] = P

    if winner(b)==P:
        print_board(b); print("AI wins"); break
    if not moves_left(b):
        print_board(b); print("Draw"); break
