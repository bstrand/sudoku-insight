sudoku-solver
=========
## Summary
A [sudoku] puzzle solver. Takes CSV input of sudoku puzzle, finds a solution through a backtracking search algorithm. 

Solutions are output to the console and written out to CSV file named '<puzzle file name>.solution'

Timing information can be added to the console output. A novelty 'watch' mode has been added that allows one to watch the algorithm move through guesses. Note that this mode greatly slows down solution.

## Requirements

* Python - Written for 2.7, untested on 3.x
* [NumPy] - The NumPy library must be installed

## Usage
sudoku-solver.py [-h] [-w] [-t] [--debug] file [file ...]

  **-w, --watch**  Watch a hacky, slightly-better-than-nothing graphical view of the puzzle being solved. _WARNING: significantly slower!_

  **-t, --timer** Track time spent solving the puzzle

  **--debug**     Write debug output.

  **-h, --help**   HALP

## Notes
This solver performs suitably on puzzles in the easy to moderate difficulty range, completing in 1-10 seconds. Especially difficult puzzles, however, can take upwards of 10 minutes to solve.

### Shortcomings 

The algorithm as implemented is rather brute force. Guesses are naive and could be improved with a number of strategies.

The visualization of the solution is, in the parlance of our times, the minimum viable.

### Next steps

* Refactor into object oriented implementation
* Improve comments
* Unit tests
* Aggregate metrics for runs against multiple puzzles
* Support for one line puzzle defition to Insight CSV
* Proper graphical rendering of puzzle & solution
* Live rendering of solution search
* Alternate algorithms
  * Constraint propagation
  * Exact cover
  * ?
* Detect multiple solutions
* Web API for solver
* Web interface for solver
* Docker container for solver

[sudoku]:https://en.wikipedia.org/wiki/Sudoku
[numpy]:http://www.numpy.org/
