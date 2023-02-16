import sys
import os
import time

def clear_screen():
    """
    Detect operating system and clear terminal
    """
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear') #Mac or Linux

def multiplayer():
    """ multiplayer game"""
    play1 = Player(input('Player one name: '))
    play2 = Player(input('Player two name: '))

    print("Welcome aboard %s and %s" % (play1,play2))
    start = input("Enter to begin ")
    clear_screen()

    print(str(play1) + "'s configuration")
    print()
    board1 = Board()
    Placer(board1)
    boardg1 = Board()

    mart = input("Hit enter to switch turns")
    clear_screen()

    print(str(play2) + "'s configuration")
    print()
    board2 = Board()
    Placer(board2)
    boardg2 = Board()

    gameend = False
    while not gameend:
        playtime(play1,board1,boardg1,board2)
        if board2.shipcount() == 0:
            print("Game Over! %s Wins" % play1)
            time.sleep(2)
            gameend = True

        playtime(play2,board2,boardg2,board1)
        if board1.shipcount() == 0:
            print("Game Over! %s Wins" % play2)
            time.sleep(2)
            gameend = True

def Placer(board):
    """platform for putting ships on the board"""
    shiptype = {
    'Carrier':5,
    'Battleship':4,
    'Cruiser':3,
    'Submarine':3,
    'Destroyer':2,
    }
    for i in (shiptype.keys()):
        contin = False
        while not contin: ##idk how to make try go back
            print(board)
            print()
            print('Ship, Holes')
            print(i, shiptype[i])
            side = input("Do you want to place the boat horizontally (1) or vertically (2) ? ")
            if side == '1':
                clear_screen()
                Horizontal(shiptype[i],board)
                contin = True
            elif side == '2':
                clear_screen()
                Vertical(shiptype[i],board)
                contin = True
            else:
                print('Invalid input')
                time.sleep(1)
                clear_screen()
            clear_screen()

def Horizontal(holes,board):
    """places horizontal ships"""
    print(board)
    print()
    print('Holes: ' + str(holes))
    print()
    ind = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9
    }

    cont1 = False
    while not cont1:
        try:
            choice2 = input('Enter a row (a-j): ')
            mox = ind[choice2] ## mox is the index of the row
            cont1 = True ##lets me move on if i enter a letter from a - j
        except:
            print("Invalid input")
            time.sleep(1)
            clear_screen()
    print(board[mox])
    # cont1 = False
    # while not cont1:

    cont2 = False
    while not cont2:
        cho1 = input('Enter number to begin range (1-10): ')
        cho2 = input('Enter number to end range (1-10): ')

        try:
            start = int(cho1) - 1 ##correcting the index and making it a int from string
            end = int(cho2) ## range better not go up to this
            if end - start == holes:

                newling = []
                for i in range(10):
                    if i in range(start,end):

                        if board[mox][i] == 'X':
                            erooerr
                        else:
                            newling.append('X')
                    else:
                        newling.append(board[mox][i]) ##row, the number of the range
                cont2 = True


        except: ##messy but this is for when cho can't be an integer
            print("Invalid input")
            time.sleep(1)


    board.edit(newling,mox)

def Vertical(holes,board):
    """places vertical ships"""
    print(board)
    print()
    print('Holes: ' + str(holes))
    print()

    cont1 = False
    while not cont1:
        choi = input('Enter a column (1-10): ')
        try:
            choi = int(choi) -1
            for i in range(10):
                col1 = board[i][choi]
                print(col1)
            cont1 = True
        except:
            print('Invalid input')
            time.sleep(1)


    ind = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9
    }

    cont2 = False
    while not cont2:
        cho1 = input('Enter letter to begin range (a-j) : ')
        cho2 = input('Enter letter to end range (a-j): ')

        try:
            mox = ind[cho1]
            dox = ind[cho2]
            if dox - mox == holes-1:

                newling = []
                for i in range(10):
                    if i in range(mox,dox+1):

                        if board[i][choi] == 'X':
                            bemememakkingerror
                        else:
                            newling.append('X')
                    else:
                        newling.append(board[i][choi])
                cont2 = True

        except:
            print('Invalid input')
            time.sleep(1)

    board.edit2(choi,newling)

def playtime(player,own,guessb,enemyb):
    cont = False
    while not cont:
        clear_screen()
        print(str(player) + "'s turn")
        print()
        print(guessb)
        print()
        print("1.Attack")
        print("2.View own board")
        print()
        choice = input('Enter: ')
        if choice == '2':
            clear_screen()
            showboard(own)
        elif choice == '1':
            cont = True
        else:
            print("Invalid input")
    cont2 = False
    while not cont2:
        ee = input("Enter row to strike(a-j): ")
        mod = input("Enter column to strike(1-10): ")
        ind = {
        'a':0,
        'b':1,
        'c':2,
        'd':3,
        'e':4,
        'f':5,
        'g':6,
        'h':7,
        'i':8,
        'j':9
        }
        try:
            yee = ind[ee] ##letters beocme number
            xee = int(mod)-1 ##numbers get shrunk
            if enemyb[yee][xee] == 'X':
                print()
                print('HIT')
                print()
                guessb.striker(enemyb,yee,xee)
                cont2 = True
            else:
                print()
                print('MISS')
                print()
                guessb.sto(yee,xee)
                cont2 = True
        except:
            print("Invalid input3")
            time.sleep(1)


    print(guessb)
    print()
    start = input("Hit enter to switch turns")

def showboard(board):
    """shows board briefly"""
    print(board)
    print()
    exit = input('Enter to return')
    clear_screen()

class Coord:
    """helps make string coordinates into objects"""
    def __init__(self,row,col):
        """constructor"""
        self.row = row ##letters are row
        self.col = col ##numbers are columns

    def __str__(self):
        """string representation"""
        return ('%s%s') % (self.row , self.col)

    def __repr__(self):
        """represents self instead of class object idk"""
        return str(self)

class Board:
    """my holy grail of this entire project"""
    def __init__(self):
            """constructor"""
            self.board = []
            alp = 'abcdefghij'
            for row in alp:
                new = []
                for col in range(1,10+1):
                    coord1 = Coord(row,col)
                    new.append(coord1)
                self.board.append(new)

    def __str__(self):
        """return as string"""
        for n in range(9):
            print(self.board[n])
        return str(self.board[9])

    def __getitem__(self,item):
        """lets me index the object"""
        return self.board[item]

    def edit(self,new,index): ##uses a new list and the index of where to put list
        """edits the board horizontally"""
        self.board.pop(index)
        return self.board.insert(index,new)

    def edit2(self,indey,new):
        """edits the board vertically"""
        for i in range(len(new)):
            self.board[i].pop(indey)
            self.board[i].insert(indey,new[i])
        return

    def striker(self,oth,y,x):
        """replaces coord with hit markerss ahhhh"""
        oth.board[y].pop(x)
        oth.board[y].insert(x,'O')
        self.board[y].pop(x)
        self.board[y].insert(x,'X')


    def sto(self,y,x):
        """replaces with miss marker"""
        self.board[y].pop(x)
        self.board[y].insert(x,'o')

    def shipcount(self):
        acc = 0
        for n in range(10):
            for i in range (10):
                if self.board[n][i] == 'X':
                    acc = acc + 1
        return acc

class Player:
    """saves a player's name"""
    def __init__(self,name):
        """ constructor"""
        self.name = name

    def __str__(self):
        """returns as string"""
        return ('%s') % self.name
