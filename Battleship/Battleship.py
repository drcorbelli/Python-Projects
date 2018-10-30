## 1. Validate all if/else paths
## 2. Validate J/10 Row/Col
## 3. List adds on Failure
## 4. Player 2
## 5. Hit phase and turns
## 6. GitHub
#Program to play Battleship
import os
from string import Template
import copy 

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
err_templ = Template("${error} - Please try again.")
ship_templ = Template("${error} - Please try again.")

def clear():
    os.system( 'cls' )

class Player:
    def __init__(self):
        #self.remaining = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        self.remaining = ["Destroyer"]
        self.ship_list = []
        self.board = []
        self.enemy = []


class Ship:
    def __init__(self, n, l, s):
        self.name  = n
        self.length = l
        self.spaces = s


#Convert Row input to integer for array
def ret_num(s):     
    for i in range(len(rows)):
        if( rows[i] == s):
            return i+1
    return 0 


#Validate position choice
def check_board(board, length, r, c, o):
    if (board[r][c] == "[ ]"):
        if(o == "Horizontal"):
            if(length <= 11 - c):
                for i in range(0,length):               # VALIDATE HIT END OF ROW/COLUMN
                    if (board[r][c+i] != "[ ]"):
                        return False
                    #else:
                    return True
            else:
                print("Ship does not fit on board - Check")
        elif(o == "Vertical"):
            if(length <= 11 - r):
                for i in range(0,length):
                    if (board[r+i][c] != "[ ]"):
                        return False
                    #else:
                    return True
            else:
                print("Ship does not fit on board - Check")
    else:
        return False


def place_ship(board, length, r, c, o):
    #print(length)
    #print(r)
    #print(c)
    #print(o)
    if(o == "Horizontal"):
        if(length <= 11 - c):
            for i in range(0,length):
                if (board[r][c+i] == "[ ]"):
                    board[r][c+i] = "[X]"
                    #print_board(board)
                   
                else:
                    return board
            return board
        else:
            print("Ship does not fit on board")
    elif(o == "Vertical"):
        if(length <= 11 - r):
            for i in range(0,length):
                if (board[r+i][c] == "[ ]"):
                    board[r+i][c] = "[X]"
                    #print_board(board)
                    #print(i)
                else:
                    print("REEEEE")
                    return board
            return board
        else:
            print("Ship does not fit on board")
    else:
        print("Orientation Missing")
        return board


def init_player():
    player = Player()
    player.board = [[" ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", "10 "],
               ["A", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["B", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["C", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["D", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["E", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["F", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["G", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["H", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["I", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
               ["J", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]]
    player.enemy = copy.deepcopy(player.board)
    print_board(player.board)
    while (len(player.remaining) != 0):
        for i in range(len(player.remaining)):
            print(player.remaining[i], end=' ')
        print()
        choose_ship = input("Choose a ship to place on board: ")
        if (player.remaining.__contains__(choose_ship)):
            print(choose_ship + " to be added.")
            player = add_ship(player, choose_ship)
            #player.ship_list.append(add_ship(player, choose_ship))                   #Figure out logic for adding ships/choosing spaces
            while choose_ship in player.remaining: player.remaining.remove(choose_ship)
            #print(len(player.ship_list))
            #print_ship_spaces(player.ship_list[(len(player.ship_list))-1])
            #print(player.ship_list[(len(player.ship_list))-1].spaces)
            #clear()
            print_board(player.board)
    return player


def setBoard(player):
    is_complete = 0
    while(not is_complete):
        test


def print_board(board):
    for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=' ')
            print()

def print_full_board(player):
    for i in range(len(player.board)):
            for j in range(len(player.board[i])):
                print(player.board[i][j], end=' ')
            print("  |  ", end=' ')
            for k in range(len(player.enemy[i])):
                print(player.enemy[i][k], end=' ')
            print()


def print_remaining_ships(player):
    print("Enemy Ships Remaining:", end=' ')
    for i in range(len(player.ship_list)):
        print (player.ship_list[i].name + ",", end=' ')
    print()


def ship_len(name):
    if (name == "Carrier"):
        return 5
    elif(name == "Battleship"):
        return 4
    elif(name == "Cruiser"):
        return 3
    elif(name == "Submarine"):
        return 3
    elif(name == "Destroyer"):
        return 2
    else:
        return 0


def calc_ship_spaces(length, int_row, int_col, orientation):
    spaces = []
    for i in range(length):
        if (orientation == "Horizontal"):
            spaces.append([int_row,int_col+i])
        elif (orientation == "Vertical"):
            spaces.append([int_row+i,int_col])
    return spaces

def print_ship_spaces(ship):
    for i in range(len(ship.spaces)):
        print(ship.spaces[i], end=" ")
    print()


def add_ship(player, name):                                        #Figure out logic for adding ships/choosing spaces
    length = ship_len(name)
    while True:
        row = input("Choose a Row to Place the Ship: ")
        if (rows.__contains__(row)):
            int_row = ret_num(row)
            column = input("Choose a Column to Place the Ship: ")
            if (columns.__contains__(column)):
                int_col = int(column)
                orientation = input("Horizontal or Vertical: ")
                if (orientation == "Horizontal"): 
                    if(check_board(player.board, length, int_row, int_col, orientation)):
                        player.board = place_ship(player.board, length, int_row, int_col, orientation)
                        spaces = calc_ship_spaces(length, int_row, int_col, orientation)
                        #print(spaces)
                        player.ship_list.append(Ship(name, length, spaces))
                        break
                    else:
                        print("Failed to add ship - Please Try Again")
                elif (orientation == "Vertical"): 
                    if(check_board(player.board, length, int_row, int_col, orientation)):
                        player.board = place_ship(player.board, length, int_row, int_col, orientation)
                        spaces = calc_ship_spaces(length, int_row, int_col, orientation)
                        player.ship_list.append(Ship(name, length, spaces)) 
                        break
                    else:
                        print("Failed to add ship - Please Try Again")
                else:
                    print("Invalid Orientation - Please Choose Again")
            else:
                    print("Invalid Column - Please Choose Again")
        else:
                    print("Invalid Row - Please Choose Again")    
    return player


def attack_ship(p1, p2):
    while True:
        row = input("Choose a Row to Hit: ")
        if (rows.__contains__(row)):
            int_row = ret_num(row)
            column = input("Choose a Column to Hit: ")
            if (columns.__contains__(column)):
                int_col = int(column)
                if(p1.enemy[int_row][int_col] == "[ ]"):        #If space already tried
                    if(p2.board[int_row][int_col] == "[ ]"):    #Miss case
                        p1.enemy[int_row][int_col] = "[-]"
                        p2.board[int_row][int_col] = "[-]"
                        break
                    elif(p2.board[int_row][int_col] == "[X]"):  #Hit case
                        p1.enemy[int_row][int_col] = "[X]"
                        p2.board[int_row][int_col] = "[O]"
                        is_sunk(p2, int_row, int_col)
                        break
                    else:
                        print("Prolems")
                else:
                    print("Space already used - Choose again")
            else:
                print("Invalid Column - Please Choose Again")
        else:
            print("Invalid Row - Please Choose Again")
    return p1,p2


def is_sunk(player, row, column):
    for i in range(len(player.ship_list)):
        for j in range(len(player.ship_list[i].spaces)):
            if ([row, column] == player.ship_list[i-1].spaces[j-1]):
                print ("YOU HIT ONE")
                del player.ship_list[i-1].spaces[j-1]
                if (player.ship_list[i-1].spaces == []):
                    print("You Sunk Enemy " + player.ship_list[i-1].name + "!")
                    del player.ship_list[i-1]
    

def two_player(p1, p2):
    turn = 1
    while (len(p1.ship_list) != 0) and (len(p2.ship_list) != 0):
        if(turn):
            print_remaining_ships(p2)
            print_full_board(p1)
            p1,p2 = attack_ship(p1,p2)
            #clear()
            print_full_board(p1)
            input("Press any Enter to end turn")
            turn = not turn
        else:
            print_remaining_ships(p1)
            print_full_board(p2)
            p2,p1 = attack_ship(p2,p1)
            #clear()
            print_full_board(p2)
            input("Press any Enter to end turn")
            turn = not turn
    return

def main():
    input("Press any Enter to begin Player 1 Setup")
    p1 = init_player()
    input("Press any Enter to begin Player 2 Setup")
    p2 = init_player()
    input("Press any Enter to start game")
    two_player(p1, p2)


if __name__ == "__main__":
    main()