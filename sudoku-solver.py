__author__ = 'bstrand'
# Sudoku solver
# Terms:
#   cell  - A square containing a single value
#   grid  - An entire sudoku puzzle, 9 cells by 9 cells
#   block - A subunits of the full grid, 3 cells by 3 cells, aligned at 3 cell strides
#
# Conventions
#   Cells are referenced by (row, column) with 0-based indices
#
# Usage
# TODO
# Takes a
#


import argparse
import numpy as np
import os

def parse_args():
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument('puzzle_files', metavar='file', nargs='+',
                        help='File(s) containing puzzle to solve')
    parser.add_argument("-w", "--watch",
                        help="Watch a hacky, slightly-better-than-nothing graphical view of the puzzle being solved. WARNING: significantly slower",
                        action="store_true")
    parser.add_argument("--debug", help="Write debug output.", action="store_true")
    args = parser.parse_args()
    if args.debug:
        print "Args parsed."
        print "Puzzle files: "
        for filename in arguments.puzzle_files:
            print "\t", filename
    return args


def load_puzzle(filename):
    puzzle = np.loadtxt(filename, dtype=int, delimiter=',')
    if args.debug:
        print "Puzzle file %s loaded, shape: %r" % (filename, puzzle.shape)
        print puzzle
    return puzzle


def is_valid_puzzle(puzzle):
    valid = True

    # 9x9 grid
    if puzzle.shape != (9, 9):
        print "Invalid puzzle grid, must be 9x9"
        valid = False

    # Valid cell values are integers 0-9
    it = np.nditer(puzzle, flags=['multi_index'])
    while not it.finished:
        if it[0] not in range(10):
            print "Invalid cell value %d in cell <%s>" % (it[0], it.multi_index)
            valid = False
        it.iternext()

    return valid


def solve_puzzle(grid):
    orig_grid = grid.copy()  # TODO necessary?
    return solve_puzzle_recurse(grid)


def solve_puzzle_recurse(grid):
    """
    Find a blank cell, find a value valid for that cell in current grid, then recurse.
    Return false in the event proposed state is unsolvable, signaling need to backtrack,
    i.e. try next value in caller's sequence
    :param grid: Sudoku puzzle grid
    :return: Solved grid or False if unresolvable
    """

    if args.watch:
        os.system('clear')
        print grid

    blank = find_blank_cell(grid)
    if not blank:
        print "-------SOLVED--------"
        if not args.watch:
            print grid
        return True

    for v in range(1,10):
        grid[blank] = v
        if is_cell_valid(grid, blank):
            solution = solve_puzzle_recurse(np.copy(grid))
            if solution:
                return solution
    return False


def is_cell_valid(grid, cell):
    (col, row) = cell

    # Check column & row for other cells with this value
    for i in range(9):
        if grid[i][row] == grid[cell] and col != i:
            return False
        if grid[col][i] == grid[cell] and row != i:
            return False

    # Check cell's block for other cells with this value
    block = [(i, j) for i in range(3*(col/3), 3+3*(col/3)) for j in range(3*(row/3), 3+3*(row/3))]
    for neighbor in block:
        if(grid[neighbor] == grid[cell] and neighbor != cell):
            return False

    if args.debug:
        print "%d -> (%d, %d)" % (grid[cell], col, row)
    return True


def find_blank_cell(grid):
    it = np.nditer(grid, flags=['multi_index'])
    while not it.finished:
        if it[0] == 0:
            return it.multi_index
        it.iternext()

    # No blank cells found, must be complete
    return False

if __name__ == "__main__":
    args = parse_args()
    print "+++ Sudoku Solver +++"
    for puzz_file in args.puzzle_files:
        print "--------------------"
        print "Solving the puzzle in %s" % puzz_file
        puzz = load_puzzle(puzz_file)
        if not is_valid_puzzle(puzz):
            print "Invalid puzzle!"
            exit
        if not solve_puzzle(puzz):
            print "No solution found. =/"