# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:30:41 2016

@author: BOSS
"""

class Play(object):
    
    board=[]
    def __init__(self,game_name):
        self.game_name= game_name     
        
    def create_board(self,no_of_rows,no_of_cols):
        for i in range (0,no_of_rows):
            self.board.append([" ---"]*no_of_cols)
            self.board.append(["| - "]* no_of_cols + ["|"])
    
        self.board.append([" ---"]* no_of_cols)
        print "Welcome to "+ self.game_name
        print ""

    def print_board(self):
        for row in self.board:
            print "".join(row)

    def prints(self,player):
       print "its " + player + " turn"
       print ""
      



class Processing(object):
    
    def __init__(self):
       pass 
    
    def choose_slot(self, position):
        while True:
            try:
                inp=int(raw_input("Choose "+ position +":"))
                if  0<inp <= 3 :
                    break  
            except ValueError:
                print """
*** That's not an int! ***"""                
            else:
                    print """
*** NOT in Range ***   """
        return inp     
    
    def row_skip(self,row,col):
        if row==1 :
            row=row
        elif row== 2:
            row=row+1
        else:
            row=row+2
        col=col-1
        
        return [row,col]
        
    def overlap_check(self,row,col,board):
        player = board[row][col]
        if player == "| X " or player == "| O ":
            
            print """
*** Its already filled, choose another slot ***"""
            
        else: 
            return True
    
    def win_check(self,obj,board):
        if board[3][1] == board [1][0] == board [5][2]== "| "+obj+" " or board[3][1] == board [1][2] == board [5][0]== "| "+obj+" ":
            return True 
        
        row=-1
        for r in range(0,3):
            row=row+2        
            if board[row][0] == board [row][1] == board [row][2]== "| "+obj+" ":
                return True 
            
        for col in range(0,3):
            if board[1][col] == board [3][col] == board [5][col]== "| "+obj+" ":
                return True
            
           
            
class Modify(object):
   def __init__(self):
       pass
         
   def move(self,row,col,board,character):
       board[row][col]= "| "+character+" "




game_initiate= Play("TicTacToe")
board= game_initiate.board
game_initiate.create_board(3,3)
game_initiate.print_board()
player= ["X","O"]

for turn in range (1,6):
    for pl in player:
        game_initiate.prints(pl)
        game_play= Processing()
        real_position= game_play.row_skip(game_play.choose_slot("row"), game_play.choose_slot("column"))
        overlap= game_play.overlap_check(real_position[0], real_position[1], Play.board)
        
        while overlap is not True:
            real_position= game_play.row_skip(game_play.choose_slot("row"), game_play.choose_slot("column"))
            overlap= game_play.overlap_check(real_position[0], real_position[1], Play.board)
        
        apply_choice= Modify()
        apply_choice.move(real_position[0], real_position[1], board, pl)
        print ""
        game_initiate.print_board()
        check= game_play.win_check(pl, board)
        
        if check is True:
            break
        elif turn==5:
            print "its a DRAW"
            break
    
    if check is True:
        print "Player " + pl + " Won... CONGRATS!"
        break