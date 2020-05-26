class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):
        valid_input = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        while True:
            position = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            if position.upper() in valid_input:
                if board.isempty(valid_input.index(position.upper())):
                    board.set(valid_input.index(position.upper()), self.sign)
                    break
                else:
                    print("You did not choose correctly.")
            else:
                print("You did not choose correctly.")
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.get_size(), board.isempty(index), and board.set(index, sign)
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can do the conversion here in the player.py or in the board.py
        # this implemenation is up to you
