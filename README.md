# Python-based-tic-tac-toe-game
I made this tic tac toe game as a final project from the course Programming Essentials in Python Part 1 by Cisco Networking Academy in collaboration with OpenEDG Python Institute.

The task is to write **a simple program that pretends to play tic-tac-toe with the user**. Here are the assumptions:

- the computer (your program) shloud play the game using 'X's (don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game);
- the user (you) shloud play the game using 'O's;
- the first move belongs to the computer - it always puts its first 'X' in the middle of the board;
- all the squares are numbered row by row startinng with 1;
- the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
- the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
- the computer responds with its move and the check is repeated;
- don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

# Bugs and bad practices

The program has a few bugs and bad practice things that I will be fixing:

**Bugs identified until now:**

- [ ] After an odd number of invalid movements (made by the user) the machine skips its turn.

 **Bad practices identified until now:**
 
 - [ ] All functions and the main program are in the same file.
 - [ ] There are variables names in spanish and english.
 - [ ] There are some variables in snake case and others in camel case.
 - [ ] Variables with no meaningful names.
 - [ ] The program should have more comments describing what each part of the program does.
