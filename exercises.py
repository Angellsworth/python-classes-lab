# Step 1) define class blueprint
class Game: #I am creating a blueprint
    def __init__(self): #this is a CONSTRUCTOR, the start of the function "defining a function" and init/initializing 
        self.turn = 'X' #first player to go will be the value of 'X'- the current player
        self.tie = False # We do not start with tie, we can flip to true later
        self.winner = None # We do not start with a winner, can change later
        self.board = { # dictionary with collection of key/value pairs - creating board, each space has a key and value
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
            }
# Step 2) Start Game play    
    #Method to start game play
    def play_game(self):
        print('Welcome to Tic-Tac-Toe!') #Welcome to the game 

        while not self.winner and not self.tie:
            self.print_board() #show the board
            self.print_message() #whose turn is it
            self.get_move() #make a move
            self.check_for_winner() #check for winner
            self.check_for_tie() #check for tie
            if not self.winner and not self.tie:
                self.switch_turn() #switch turns
                
        self.print_board() #update board
        self.print_message()
        

# Step 3) Print board
    def print_board(self): #Method to print the board
        b = self.board #create a shortcut variable for cleaner code
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            -----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            -----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
# Step 4) Track whose turn, tie, winner messages
    def print_message(self):
        if self.tie:
            print("Tie game!") #if tie set to True
        elif self.winner:
            print(f"{self.winner} wins the game!") #if winner print winner
        else:
            print(f"It is player {self.turn}'s turn!") #no tie or winner print next player turn
# Step 5) Handle Player input
    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower() #ask the player for a move
            if move not in self.board:
                print("That's not on the board. Try again.") #if spot is not on the board
            elif self.board[move] is not None:
                print("Nice try, but that spot is taken. Try again.") #if spot is taken
            else:
                self.board[move] = self.turn #take the spot
                break #stop loop next player or win or tie message
# Step 6) Switch players
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X' #ternary expression -If it’s X, make it O. Else, make it X.
# Step 7) Check for winner
    def check_for_winner(self):
        combos = [ #listing out all 8 winning possibilities
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3']
        ]
        for combo in combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None: #are spaces equal? if yes win, if not move on
                self.winner = self.turn #record winner on whose turn it was
# Step 8) Check for tie
    def check_for_tie(self):
        if not self.winner and all(space is not None for space in self.board.values()):#if spaces are filled but don't match
            self.tie = True #flip to tie

    
#Instantiate and start the game
game_instance = Game()
game_instance.play_game()#calls welcome message

