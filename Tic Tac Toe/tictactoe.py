import numpy as np

#empty array 3x3
board = np.ones((3,3)) * 10

#player-1
def player_1(i,j):
	if board[i,j] == 1 or board[i,j] == 0:
		
		print 'please enter valid input'
		print board
	
	else:
		board[i,j] = 1

#player-2
def player_2(i,j):
	if board[i,j] == 1 or board[i,j] == 0:
		
		print 'please enter valid input'
		print board
	
	else:
		board[i,j] = 0
		
def score_check():
    if board[0,0]+board[0,1]+board[0,2] == 3:
        print 'player_1 wins'
        exit()
    elif board[0,0]+board[0,1]+board[0,2] == 0:
        print 'player_2 wins'
        exit()
    elif board[1,0]+board[1,1]+board[1,2] == 3:
        print 'player_1 wins'
        exit()
    elif board[1,0]+board[1,1]+board[1,2] == 0:
        print 'player_2 wins'
        exit()
    elif board[2,0]+board[2,1]+board[2,2] == 3:
        print 'player_1 wins'
        exit()
    elif board[2,0]+board[2,1]+board[2,2] == 0:
        print 'player_2 wins'
        exit()
    elif board[0,0]+board[1,0]+board[2,0] == 3:
        print 'player_1 wins'
        exit()
    elif board[0,0]+board[1,0]+board[2,0] == 0:
        print 'player_2 wins'
        exit()
    elif board[0,1]+board[1,1]+board[2,1] == 3:
        print 'player_1 wins'
        exit()
    elif board[0,1]+board[1,1]+board[2,1] == 0:
        print 'player_2 wins'
        exit()
    elif board[0,2]+board[1,2]+board[2,2] == 3:
        print 'player_1 wins'
        exit()
    elif board[0,2]+board[1,2]+board[2,2] == 0:
        print 'player_2 wins'
        exit()
    elif board[0,0]+board[1,1]+board[2,2] == 3:
        print 'player_1 wins'
        exit()
    elif board[0,0]+board[1,1]+board[2,2] == 0:
        print 'player_2 wins'
        exit()
    elif board[2,0]+board[1,1]+board[0,2] == 3:
        print 'player_1 wins'
        exit()
    elif board[2,0]+board[1,1]+board[0,2] == 0:
        print 'player_2 wins'
        exit()
    

#game loop
i=1
while i<=9:
    
    print 'move number',i
    print 'player-1 plays'

    one_i = input('Enter your input i: ')
    one_j = input('Enter your input j: ')    
    
    player_1(one_i,one_j)
    
    print board
    
    score_check()
    
    i+=1
    
    print 'move number',i
    print 'player-2 plays'
    
    zero_i = input('Enter your input i: ')
    zero_j = input('Enter your input j: ')
    
    player_2(zero_i,zero_j)
    
    print board
    
    score_check()