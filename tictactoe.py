import random
import os

#setup board as completely blank
boardList=[0,0,0,0,0,0,0,0,0]

#rows: A1, B1, B1, A, B, C, D1, D2 
rowlist_player=[0,0,0,0,0,0,0,0]
rowlist_computer=[0,0,0,0,0,0,0,0]

#display the board
print boardList[6:9]
print boardList[3:6]
print boardList[0:3]

def LoopBackPlayer():
    PlayerMove()

def PlayerMove():

    os.system('cls' if os.name == 'nt' else 'clear')
    #display the board
    print("")
    print boardList[6:9]
    print boardList[3:6]
    print boardList[0:3]
    print ""
    print rowlist_player[7]
    print rowlist_player[5]
    print rowlist_player[4]
    print rowlist_player[3]
    print rowlist_player[6], rowlist_player[0:3]


    #get user input for move
    PlayerMove = input("Go: ")

    if PlayerMove < 9:
        if boardList[PlayerMove] is not 0:
            print("That space is taken!")
            LoopBackPlayer()
    else:
        LoopBackPlayer()
    #edit board to account for move
    boardList[PlayerMove] = 1



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
        print("YOU WIN!!!!")





def ComputerMove():

    # if PlayerMove is 0:
    #     rowlist_player[0]=(rowlist_player[0]+1)
    #     rowlist_player[3]=(rowlist_player[3]+1)
    #     rowlist_player[6]=(rowlist_player[6]+1)
    # if PlayerMove is 1:
    #     rowlist_player[1]=(rowlist_player[1]+1)
    #     rowlist_player[3]=(rowlist_player[3]+1)
    # if PlayerMove is 2:
    #     rowlist_player[2]=(rowlist_player[2]+1)
    #     rowlist_player[3]=(rowlist_player[3]+1)
    #     rowlist_player[7]=(rowlist_player[7]+1)
    # if PlayerMove is 3:
    #     rowlist_player[0]=(rowlist_player[0]+1)
    #     rowlist_player[4]=(rowlist_player[4]+1)
    # if PlayerMove is 4:
    #     rowlist_player[1]=(rowlist_player[1]+1)
    #     rowlist_player[4]=(rowlist_player[4]+1)
    #     rowlist_player[6]=(rowlist_player[6]+1)
    #     rowlist_player[7]=(rowlist_player[7]+1)
    # if PlayerMove is 5:
    #     rowlist_player[2]=(rowlist_player[2]+1)
    #     rowlist_player[4]=(rowlist_player[4]+1)
    # if PlayerMove is 6:
    #     rowlist_player[0]=(rowlist_player[0]+1)
    #     rowlist_player[5]=(rowlist_player[5]+1)
    #     rowlist_player[7]=(rowlist_player[7]+1)
    # if PlayerMove is 7:
    #     rowlist_player[1]=(rowlist_player[1]+1)
    #     rowlist_player[5]=(rowlist_player[5]+1)
    # if PlayerMove is 8:
    #     rowlist_player[2]=(rowlist_player[2]+1)
    #     rowlist_player[5]=(rowlist_player[5]+1)
    #     rowlist_player[6]=(rowlist_player[6]+1)

    print("I moved")
    if max(rowlist_computer) < 3:
        PlayerMove()
    else:
        print("YOU LOSE!!!!")


PlayerMove()


