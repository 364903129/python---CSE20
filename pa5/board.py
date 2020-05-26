def isfull(board):
    for i in board:
        if i == " ":
            return False
    return True


class Board:
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        self.winner = ""

    def get_size(self):
        # return the board size (an instance size)
        return self.size

    def get_winner(self):
        # return the winner (a sign O or X) (an instance winner)
        return self.winner

    def set(self, index, sign):
        # mark the cell specified by the index with the sign (X or O)
        self.sign = sign
        self.board[index] = sign

    def isempty(self, index):
        # return True if the cell specified by the index is empty (not marked with X or O)
        board = self.board
        if board[index] == " ":
            return True
        else:
            return False

    def isdone(self):
        done = False
        win = False
        board = self.board
        if board[0] == board[1] == board[2] != " " or board[0] == board[4] == board[8] != " " or board[0] == board[3] == \
                board[6] != " " or \
                board[1] == board[4] == board[7] != " " or board[2] == board[4] == board[6] != " " or board[2] == board[
            5] == board[
            8] != " " or board[3] == board[4] == board[5] != " " or board[6] == board[7] == board[8] != " ":
            done = True
            win = True
        if isfull(board):
            done = True

        if win and done:
            if self.sign == 'O':
                self.winner = 'O'
            elif self.sign == 'X':
                self.winner = 'X'
        else:
            self.winner = 'tie'
        return done

    def show(self):
        # draw the board
        input1 = ["1", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|"]
        input2 = ["2", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|"]
        input3 = ["3", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|"]
        # a1 a2 a3 = input1[4], input2[4], input3[4]
        # b1 b2 b3 = input1[8], input2[8], input3[8]
        # c1 c2 c3 = input1[12], input2[12], input3[12]
        line1 = self.board[0:9:3]
        line2 = self.board[1:9:3]
        line3 = self.board[2:9:3]
        for i in range(len(line1)):
            if line1[i] != " ":
                input1[(i + 1) * 4] = self.board[i * 3]
        for j in range(len(line2)):
            if line2[j] != " ":
                input2[(j + 1) * 4] = self.board[(j * 3 + 1)]
        for k in range(len(line3)):
            if line3[k] != " ":
                input3[(k + 1) * 4] = self.board[k * 3 + 2]
        print()
        print("    A   B   C ")
        print("  +---+---+---+")
        print("".join(input1))
        print("  +---+---+---+")
        print("".join(input2))
        print("  +---+---+---+")
        print("".join(input3))
        print("  +---+---+---+")
