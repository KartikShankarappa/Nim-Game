
* This is a specific variant of the [Nim Game](http://en.wikipedia.org/wiki/Nim). The game has two players, the computer and a human opponent

### Game Rules
* Randomly create a number of heaps where the number must either be 3, 5 or 7
* For each heap created, randomly assign the initial number of objects within the heap. The number can be either 9, 11 or 13
* Randomly assign the first player, either the human or the computer.
* The first player removes any positive and non-zero number of objects (including all objects) for any one heap
* The second player then does the same
* Play continues, alternating turns, until no objects remain in any heap.
* The player taking the last object(s) is the winner

### Implementation
* This code is implemented in Python.
* A file named __compile.sh__ is placed in the root of the homework directory which when invoked will compile the program.
* A file named __execute.sh__ is placed in the root of the homework directory which when invoked will run the program (assuming __compile.sh__ has been invoked first).
* Upon execution your program must accept input from the command line and produce output (exactly) according to the following rules
    - Print the number of heaps created and their sizes on one line in the following format - `Created X heaps of sizes Y1 Y2 ... Yn` where X is the number of heaps created and each progressive Y is the size of the heap so if your program upon launch created 5 heaps of sizes 9, 11, 13, 11, 9 then the initial output of your program would be:
     `Created 5 heaps of sizes 9 11 13 11 9`
    - On a new line, print the name of the player to go first in the following format: `Player X goes first` where X is either `computer` or `human`. For example if player `computer` was randomly chosen to go first then the output would be:
     `Player computer goes first`
    - __Note__, the heaps will be identified by number starting with 1. So in the above example there are five heaps where the first heap (with 9 objects) is identified by __1__, the second heap (with 11 objects) is identified by __2__ and so on with the last heap in the example being labeled __5__ (with 9 objects).
* If the turn is for the computer then the following will be printed:
    - `Player computer took Y objects from heap X`
* If the turn is for the human then the following will be printed:
    - `Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X `
* After each turn your program will print the number of objects remaining in each heap, in order, e.g. if the first move the first player took 1 object from the first heap (using the values from the example above) your program would print:
    - `8 11 13 11 9`
    - If no more objects remain in a heap, 0 will be printed for its value.
* Upon game completion your program will print the winner in the format:
    - `Player X has won` where X is either `computer` or `human`
* __Note__ - if the `human` makes an incorrect move (e.g., tries to take more objects than are available in the specified heap) your program should print the following and then reprint the instruction for the human to play:
    - `Player human that is an invalid move, try again`
    - `Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X `
    
### Example Game Play
Here is an example game play assuming the following; 5 heaps were randomly created with sizes 9 11 13 11 9 and the computer was randomly chosen to go first:

* `Created 5 heaps of sizes 9 11 13 11 9`
* `Player computer goes first`
* `Player computer took 9 objects from heap 1`
* `0 11 13 11 9`
* `Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X `
* __human enters__ `5 2`
* `0 6 13 11 9`
* `Player computer took 6 objects from heap 2`
* `0 0 13 11 9`
* `Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X `
* __human enters__ `1 1`
* `Player human that is an invalid move, try again`
* `Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X `
* __human enters__ `15 3`
* `Player human that is an invalid move, try again`
* `Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X `
* __human enters__ `13 3`
* `0 0 0 11 9`
* `Player computer took 11 objects from heap 4`
* `0 0 0 0 9`
* __human enters__ `9 5`
* `0 0 0 0 0`
* `Player human has won`
