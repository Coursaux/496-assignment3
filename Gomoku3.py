#!/usr/bin/python3
#/usr/local/bin/python3
# Set the path to your python3 above

from gtp_connection import GtpConnection
from board_util import GoBoardUtil
from simple_board import SimpleGoBoard

class Gomoku():
      def __init__(self):
            """
            Gomoku player that selects moves randomly 
            from the set of legal moves.
            Passe/resigns only at the end of game.

            """
            self.name = "GomokuAssignment2"
            self.version = 1.0

      def get_move(self, board, color):
            return GoBoardUtil.generate_random_move_gomoku(board)

      def simulate_random(self,board,color):
            #get empty points from the board and simulate at random 10 times
            legal_moves = GoBoardUtil.generate_legal_moves(board,color)
            #win 2 score, draw 1 score, lose 0 score
            max_winrate = 0.0
            best_move = 0
            for move in legal_moves:
                  score = 0.0
                  for i in range(10):
                        temp_board = board.copy()
                        #play the first step
                        temp_board.play_move_gomoku(move,color)
                        #pass the board and the origianl color 
                        result = GoBoardUtil.simulate_random(temp_board,color)
                        #add up the total score
                        score+=result
                  
                  #find the winrate
                  score /= 10
                  if score>=max_winrate:
                        #evaluate if the winrate is higher than the current best move
                        max_winrate = score
                        best_move = move
            return best_move
    
    
def run():
      """
      start the gtp connection and wait for commands.
      """
      #random.seed() no need to seed because we use np.random
      board = SimpleGoBoard(7)
      con = GtpConnection(Gomoku(), board)
      con.start_connection()

if __name__=='__main__':
      run() 
