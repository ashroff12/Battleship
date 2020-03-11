WIDTH = 10
HEIGHT = 10
P1_attack = []
P2_attack = []
P1_ships = []
P2_ships = []

P1_shiplist = [
            ["A", 2, False],
            ["B", 1, False],
            ["C", 5, False],
            ["D", 3, False],
            ["E", 2, False]
         ]
P2_shiplist = [
            ["A", 2, False],
            ["B", 1, False],
            ["C", 5, False],
            ["D", 3, False],
            ["E", 2, False]
         ]
def fill_board(board):
    temprow = []
    for i in range(WIDTH):
        temprow.append('0')
    for i in range(HEIGHT):
        board.append(temprow.copy())

def show_board(board):
    for i in range(HEIGHT):
        print(board[i])
def place_ship(symbol, length, row, col, orient, board):
    if orient == "hor":
        if col + length > WIDTH:
            print("invaild ship")
            return
        else:
            for i in range(length):
                board[row][col + i] = symbol
    if orient == "vert":
        if col + length > HEIGHT:
            print("invaild ship")
            return
        else:
            for i in range(length):
                board[row + i][col] = symbol
def ship_placement(board):
    for i in range (len(P1_shiplist)):
        print("Place Ship " + P1_shiplist[i][0] + ", length" + str(P1_shiplist[i][1]))
        position = input("Position >>>")
        orient = input("Orientation >>>")
        col = ord(position[0].upper()) - 65
        row = int(position[1:]) - 1


        place_ship(P1_shiplist[i][0], P1_shiplist[i][1], row, col, orient, board)



        
def start_game():
    fill_board(P1_attack)
    fill_board(P2_attack)
    fill_board(P1_ships)
    fill_board(P2_ships)

start_game()
ship_placement(P1_attack)
show_board(P1_attack)

