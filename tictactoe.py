import random
import os

#setup board as completely blank
board=[0,0,0,0,0,0,0,0,0]

#rows: A1, B1, B1, A, B, C, D1, D2 
rowlist_player=[0,0,0,0,0,0,0,0]
rowlist_computer=[0,0,0,0,0,0,0,0]

#display the board
print board[6:9]
print board[3:6]
print board[0:3]

def LoopBackPlayer():
    PlayerMove()

def PlayerMove():

    os.system('cls' if os.name == 'nt' else 'clear')
    #display the board
    print("")
    print board[6:9]
    print board[3:6]
    print board[0:3]
    print ""
    print rowlist_player[7]
    print rowlist_player[5]
    print rowlist_player[4]
    print rowlist_player[3]
    print rowlist_player[6], rowlist_player[0:3]


    #get user input for move
    PlayerMove = input("1-Go: ")

    if PlayerMove < 9:
        if board[PlayerMove] is not 0:
            print("That space is taken!")
            LoopBackPlayer()
    else:
        LoopBackPlayer()
    #edit board to account for move
    board[PlayerMove] = 1



    # print rowlist_player[0:8]

    if PlayerMove is 0:
        rowlist_player[0]=(rowlist_player[0]+1)
        rowlist_player[3]=(rowlist_player[3]+1)
        rowlist_player[6]=(rowlist_player[6]+1)
    if PlayerMove is 1:
        rowlist_player[1]=(rowlist_player[1]+1)
        rowlist_player[3]=(rowlist_player[3]+1)
    if PlayerMove is 2:
        rowlist_player[2]=(rowlist_player[2]+1)
        rowlist_player[3]=(rowlist_player[3]+1)
        rowlist_player[7]=(rowlist_player[7]+1)
    if PlayerMove is 3:
        rowlist_player[0]=(rowlist_player[0]+1)
        rowlist_player[4]=(rowlist_player[4]+1)
    if PlayerMove is 4:
        rowlist_player[1]=(rowlist_player[1]+1)
        rowlist_player[4]=(rowlist_player[4]+1)
        rowlist_player[6]=(rowlist_player[6]+1)
        rowlist_player[7]=(rowlist_player[7]+1)
    if PlayerMove is 5:
        rowlist_player[2]=(rowlist_player[2]+1)
        rowlist_player[4]=(rowlist_player[4]+1)
    if PlayerMove is 6:
        rowlist_player[0]=(rowlist_player[0]+1)
        rowlist_player[5]=(rowlist_player[5]+1)
        rowlist_player[7]=(rowlist_player[7]+1)
    if PlayerMove is 7:
        rowlist_player[1]=(rowlist_player[1]+1)
        rowlist_player[5]=(rowlist_player[5]+1)
    if PlayerMove is 8:
        rowlist_player[2]=(rowlist_player[2]+1)
        rowlist_player[5]=(rowlist_player[5]+1)
        rowlist_player[6]=(rowlist_player[6]+1)
    
    if max(rowlist_player) < 3:
        ComputerMove()
    else:
        PlayerWins()





def ComputerMove():

    os.system('cls' if os.name == 'nt' else 'clear')
    #display the board
    print("")
    print board[6:9]
    print board[3:6]
    print board[0:3]
    print ""
    print rowlist_player[7]
    print rowlist_player[5]
    print rowlist_player[4]
    print rowlist_player[3]
    print rowlist_player[6], rowlist_player[0:3]


    #get user input for move
    PlayerMove = input("2-Go: ")

    if PlayerMove < 9:
        if board[PlayerMove] is not 0:
            print("That space is taken!")
            LoopBackPlayer()
    else:
        LoopBackPlayer()
    #edit board to account for move
    board[PlayerMove] = 1



    # print rowlist_player[0:8]

    if PlayerMove is 0:
        rowlist_computer[0]=(rowlist_computer[0]+1)
        rowlist_computer[3]=(rowlist_computer[3]+1)
        rowlist_computer[6]=(rowlist_computer[6]+1)
    if PlayerMove is 1:
        rowlist_computer[1]=(rowlist_computer[1]+1)
        rowlist_computer[3]=(rowlist_computer[3]+1)
    if PlayerMove is 2:
        rowlist_computer[2]=(rowlist_computer[2]+1)
        rowlist_computer[3]=(rowlist_computer[3]+1)
        rowlist_computer[7]=(rowlist_computer[7]+1)
    if PlayerMove is 3:
        rowlist_computer[0]=(rowlist_computer[0]+1)
        rowlist_computer[4]=(rowlist_computer[4]+1)
    if PlayerMove is 4:
        rowlist_computer[1]=(rowlist_computer[1]+1)
        rowlist_computer[4]=(rowlist_computer[4]+1)
        rowlist_computer[6]=(rowlist_computer[6]+1)
        rowlist_computer[7]=(rowlist_computer[7]+1)
    if PlayerMove is 5:
        rowlist_computer[2]=(rowlist_computer[2]+1)
        rowlist_computer[4]=(rowlist_computer[4]+1)
    if PlayerMove is 6:
        rowlist_computer[0]=(rowlist_computer[0]+1)
        rowlist_computer[5]=(rowlist_computer[5]+1)
        rowlist_computer[7]=(rowlist_computer[7]+1)
    if PlayerMove is 7:
        rowlist_computer[1]=(rowlist_computer[1]+1)
        rowlist_computer[5]=(rowlist_computer[5]+1)
    if PlayerMove is 8:
        rowlist_computer[2]=(rowlist_computer[2]+1)
        rowlist_computer[5]=(rowlist_computer[5]+1)
        rowlist_computer[6]=(rowlist_computer[6]+1)
    
    if max(rowlist_computer) < 3:
        LoopBackPlayer()
    else:
        ComputerWins()


def PlayerWins():
    os.system('cls' if os.name == 'nt' else 'clear')
    #display the board
    print("")
    print board[6:9]
    print board[3:6]
    print board[0:3]
    print ""
    print rowlist_player[7]
    print rowlist_player[5]
    print rowlist_player[4]
    print rowlist_player[3]
    print rowlist_player[6], rowlist_player[0:3]
    print("Player One Wins!!")

def ComputerWins():
    os.system('cls' if os.name == 'nt' else 'clear')
    #display the board
    print("")
    print board[6:9]
    print board[3:6]
    print board[0:3]
    print ""
    print rowlist_player[7]
    print rowlist_player[5]
    print rowlist_player[4]
    print rowlist_player[3]
    print rowlist_player[6], rowlist_player[0:3]
    print("Player Two Wins!!")

PlayerMove()


