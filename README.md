# MinesweeperAI
This is my solution for the MinesweeperAI in the Harvard's course: "Introduction to Artificial Inteligence with Python.
# Knowledge Representation
The knowledge base consists of logical sentences. 
Each logical sentence is represented by a set of positions on the board {(0,0), (0,1), (0,2)} and a variable count representing the number of mines within this set.
It is a useful representation because:

  •	We click on a tile and reveal 0. Then, for sure all the adjacent tiles are safe.
  
  •	If the count is equal to the number of positions eg.{(0,0), (0,1), (0,2)} = 3, we know that all of those are mines.
  
  •	If we know that {(0,0), (0,1), (0,2)} = 2, and {(0,0), (0,1)} = 2, we are sure that (0,2) is not a mine.
