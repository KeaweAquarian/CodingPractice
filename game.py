class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in[self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #012 etc tells what # corresponds to box
        nnumber_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' +' | ' .join(row) + ' |')

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == '']
    
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.noard.count(" ")
        
            