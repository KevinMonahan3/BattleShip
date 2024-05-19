from random import randint
import csv
from matplotlib import pyplot as plt
 


def singlePlayer():       #Definition for singleplayer mode
    
    game_board = [["O","O","O"],    #Setting up the game board
                  ["O","O","O"],    
                  ["O","O","O"]]

    def board():
 
        for i in game_board:                  #For every item in game_board puts a blank space after it
            for j in i:                       #This code was referenced from stack overflow
                print(j, end = "   ")
            print()    
 
    board()
     
    def random_row(game_board):                   #Defintion to get row and column for ship
        return randint(0, len(game_board) -1)

    def random_column(game_board):
        return randint(0, len(game_board) -1)

    ship_row = random_row(game_board)
    ship_col = random_column(game_board)
    print(ship_row) # shows ship row and column for testing
    print(ship_col)

    for turn in range(4):              #For loop that contains how the game runs
        print("Turn", turn + 1)
        guess_row = int(input("Guess a row between 0 and 2: "))          #Player guesses for ship
        guess_col = int(input("Guess a column between 0 and 2: "))
 
        if guess_row == ship_row and guess_col == ship_col:        #If player guesses right
            game_board[guess_row][guess_col] = "X" 
            board()
            print("Congratulations! You sank my battleship!")
            break
        else:
            if guess_row not in range(3) or \
            guess_col not in range(3):                #If player guesses spot not on the board
                print("Oops, that's not even in the ocean.")
            elif game_board[guess_row][guess_col] == "X":  #If the player already guessed that spot
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")         #If the player misses the battleship
                game_board[guess_row][guess_col] = "X"     #Sets the position they guessed to an X to show they have missed and what square they guessed
        if (turn == 3):                                    #Once turn == 3 game is over
            print("Game Over")
            print(f"My ship was on row: {ship_row} and column: {ship_col}")
            game_board[ship_row][ship_col] = "S" 
        board()



def multiplayer():       #Definition for two player multiplayer
    
    playerOne = input("Player one enter your name: ")
    playerTwo = input("Player two enter your name: ")
    
    player_one_game_board = [["O","O","O"],          #Player 1's game board
                             ["O","O","O"],
                             ["O","O","O"]]

    def playerOneBoard():
 
        for i in player_one_game_board:
            for j in i:
                print(j, end = "  ")
            print()
            
    player_two_game_board = [["O","O","O"],           #Player 2's game board
                             ["O","O","O"],
                             ["O","O","O"]]

    def playerTwoBoard():
 
        for i in player_two_game_board:
            for j in i:
                print(j, end = "  ")
            print()


    playerOneRow = int(input("Player one enter row between 0 and 2 for ship: "))          #Player 1's ship location
    playerOneCol = int(input("Player one enter column between 0 and 2 for ship: "))
    
    for i in range(10):      #Leaves enough blank space so player 2 can't see player 1's ship location
        print("\n")

    playerTwoRow = int(input("Player two enter row between 0 and 2 for ship: "))           #Player 2's ship location
    playerTwoCol = int(input("Player two enter column between 0 and 2 for ship: "))
    
    for i in range(10):
        print("\n")



    playerOneWin = 0          #2 variables to check wether player 1 or 2 have won
    playerTwoWin = 0
    
    
    def playerOneTurn(player_two_game_board, playerOneWin, playerTwoWin):     #Defintion for player 1's turn which contains player two's game board
        
        playerOneGuessNo = 0

        while playerOneWin != 1 and playerTwoWin != 1:        #To make sure that player 1 or 2 have not already won
            
            
            playerTwoBoard()         #Uses player 2's game board 
        
            print(f"{playerOne}'s Turn {playerOneGuessNo + 1}")
            player_one_guess_row = int(input("Guess a row between 0 and 2: "))           #Player 1's guesses
            player_one_guess_col = int(input("Guess a column between 0 and 2: "))
        
            if player_one_guess_row == playerTwoRow and player_one_guess_col == playerTwoCol:     #Same code as singleplayer
                print("Congratulations! You sank my battleship!")
                print(f"{playerOne} Wins!!!")
                playerOneWin += 1     #Variable to show player has won and to end the game
                exit()
            else:
                if player_one_guess_row not in range(3) or \
                player_one_guess_col not in range(3):
                    print("Oops, that's not even in the ocean.")
                elif player_two_game_board[player_one_guess_row][player_one_guess_col] == "X":
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    player_two_game_board[player_one_guess_row][player_one_guess_col] = "X"
                    
                    playerTwoTurn(player_one_game_board, playerTwoWin)   #If player 1 misses their guess it starts player 2's turn
                     
                     
                     
    
    def playerTwoTurn(player_one_game_board, playerTwoWin):    #Player 2's turn that contains player 1's game board
        
        playerTwoGuessNo = 0
            
        while playerTwoWin != 1:        #Will only play player 2's turn if player 1 has not won already
        
        
            playerOneBoard()      #Player 1's game board
            
            print(f"{playerTwo}'s Turn {playerTwoGuessNo + 1}")
            player_two_guess_row = int(input("Guess a row between 0 and 2: "))
            player_two_guess_col = int(input("Guess a column between 0 and 2: "))
            
            if player_two_guess_row == playerOneRow and player_two_guess_col == playerOneCol:   #Code for game is the same as singleplayer
                print("Congratulations! You sank my battleship!")
                print(f"{playerTwo} Wins!!!")
                playerTwoWin += 1      #Add to variable to show player 2 won
                exit()
            else:
                if player_two_guess_row not in range(3) or \
                player_two_guess_col not in range(3):
                    print("Oops, that's not even in the ocean.")
                elif player_one_game_board[player_two_guess_row][player_two_guess_col] == "X":
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    player_one_game_board[player_two_guess_row][player_two_guess_col] = "X"
                    playerTwoGuessNo += 1
                    
                    playerOneTurn(player_two_game_board, playerOneWin, playerTwoWin)  #If player 2 guesses wrong starts player 1's next turn
                    
                
    
    playerOneTurn(player_two_game_board, playerOneWin, playerTwoWin)   #Runs multiplayer game starting with player 1's turn
    
    
    
def computer():      #Definition for computer simulation
    
    
    NoRuns = int(input("Please enter how many times you want to run the simulation: "))   #Asks the user ho many times to run the simulation
    
    firstTurnWin = 0        #Variables for how many turns it takes for the computer to win
    secTurnWin = 0
    thirdTurnWin = 0
    lastTurnWin = 0
    noWin = 0
    
    for r in range(NoRuns):          #Runs the programme how ever many times the user asked
    
        game_board = [["O","O","O"],
                      ["O","O","O"],
                      ["O","O","O"]]

        def board():
     
            for i in game_board:
                for j in i:
                    print(j, end = "  ")
                print()    
     
        board()
        
        def random_row(game_board):         #Row for ship
            return randint(0, len(game_board) -1)

        def random_column(game_board):      #Column for ship
            return randint(0, len(game_board) -1)
        
        def guess_random_row(game_board):   #Computer's guess for row
            return randint(0, len(game_board) -1)

        def guess_random_column(game_board):   #Computer's guess for column
            return randint(0, len(game_board) -1)

        ship_row = random_row(game_board)
        ship_col = random_column(game_board)
        print(f"Ship location: {ship_row}, {ship_col}")

        for turn in range(4):     #Runs the same as singleplayer but computer guesses instead of user
       
            
            print("Turn", turn + 1)
            guess_row = guess_random_row(game_board)
            guess_col = guess_random_column(game_board)
            
            print(guess_row)
            print(guess_col)
            
            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sank my battleship!")
                print("\n")
                if turn == 0:            #Adds a value to one of the win variables so at the end it shows how many turns each win took
                    firstTurnWin += 1
                elif turn == 1:
                    secTurnWin += 1
                elif turn == 2:
                    thirdTurnWin += 1
                elif turn == 3:
                    lastTurnWin += 1                    
                break
            
            else:
                if game_board[guess_row][guess_col] == "X":
                    print("You guessed that one already.")
                    
                else:
                    print("You missed my battleship!")
                    game_board[guess_row][guess_col] = "X"
                    
            if (turn == 3):
                print("Game Over")
                noWin += 1
                
            board()
            print("\n")
    
    
    dataList = [firstTurnWin, secTurnWin, thirdTurnWin, lastTurnWin]       #Turned the win variables into a list
    noWins = firstTurnWin + secTurnWin + thirdTurnWin + lastTurnWin        #A new variable for number of wins
    
    def arithmetic_mean(L):        #An algorithm to get the mean turns to win

        total = 0

        # Now loop over the list
        for v in L:
            total = total + v # running total

        # Divide the total and number of runs added together by the number of values in L
        return (total + NoRuns)/len(L)
    
    myMean = arithmetic_mean(dataList)     #My mean of the data
    
    
    def arithmetic_mode(L):     #Algorithm to find my mode of the data
        
        uniqueValues = []       #Creates a new list for unique values
        for value in L:
            if value not in uniqueValues:      #If a value is not in the unique value list it adds it to the list
                uniqueValues.append(value)
         
        frequencies = []       #New list for frequency of values
        for value in uniqueValues:
            frequency = L.count(value)      #Counts how many times a value is in the unique values list
            frequencies.append(frequency)   #Appends that number to frequency list
            
        maxFrequency = max(frequencies)     #Gets the highest appearing number
        maxFrequencyPos = frequencies.index(maxFrequency)   #gets the index of the frequency of the highest value
        mode = uniqueValues[maxFrequencyPos]    #Gets the mode of the data
        
        return mode
    
    myMode = arithmetic_mode(dataList)    #Mode of my data
    
    def arithmetic_median(L):   #Algorithm to find the median of my data
        
        L.sort()       #Sorts the list
        
        numValues = len(L)     #Assigns the length of the list a value
        mid = numValues//2     #How it will get the median
        
        median = L[mid]        #Finds the median of my list
        
        return median

    myMedian = arithmetic_median(dataList)       #Variable for my median

    f = open('battleshipData.csv', 'a', newline='')    #Opens a csv file for the data
    writer = csv.writer(f)
    add = (NoRuns, noWins, myMean, myMedian, myMode)   #Variable to store all my data from before
    writer.writerow(add)            #Adds the data to the csv file in its own row
    
  
    dataName = ['No. of Runs', 'No. of wins', 'Mean', 'Median', 'Mode']     #Headings for the bar chart
    allData = [NoRuns, noWins, myMean, myMedian, myMode]      #Values for the bar chart
    dataList = [firstTurnWin, secTurnWin, thirdTurnWin, lastTurnWin]
                
    print("\n")
    print(f"The computer won {noWins} times in total")
    print(f"The computer won in the first turn {firstTurnWin} times")
    print(f"The computer won in the second turn {secTurnWin} times")
    print(f"The computer won in the third turn {thirdTurnWin} times")
    print(f"The computer won in the last turn {lastTurnWin} times")
    print(f"The computer did not win {noWin} times")
    print(f"The list of data {dataList}")
    print(f"The mean: {myMean}")
    print(f"The median: {myMedian}")
    print(f"The mode: {myMode}")
    
    
    plt.bar(dataName, allData)      #Creates a bar chart to convey all the data collected
    plt.title("Battle ship data")
    plt.ylabel("Data values")
    plt.xticks(range(len(dataName)), dataName)
    plt.show()
    

playerGamemode = input("Do you want to play singleplayer (S), multiplayer (M) or computer (C): ")     #Asks what version of the game the users wants to run

if playerGamemode.lower() == "s":
    singlePlayer()
elif playerGamemode.lower() == "m":
    multiplayer()
elif playerGamemode.lower() == "c":
    computer()
else:
    print("You have not chosen one of the options")







