import numpy as np
import matplotlib.pyplot as plt


def return_board(queens):
    """
    Convert a list of queen positions to a binary matrix representing the 
    placement of the queens on a chess board.

    Parameters:
    queens (list): A list of integers representing the positions of queens on the board.
                   The index of each element represents the row, and the value represents
                   the column of the queen.

    Returns:
    numpy.ndarray: A 2D binary numpy array of size N x N, where N is the length of the queens list.
                   The value 1 in the array represents a queen on that position, and 0 represents
                   an empty cell.
    """
    n = len(queens)
    board = np.zeros((n, n))
    for i, j in enumerate(queens):
        board[i, j] = 1
    return board


def plot_board(board_bin):
    
    """
    Takes a binary matrix representation of the position of queens on the chessboard and plots it on a chessboard.

    Parameters:
    - board_bin (np.array): A binary matrix of values representing the position of queens on the chessboard. 
    A value of 1 in a particular cell indicates that a queen is present in that square, while a value of 0 
    indicates that the square is empty.

    Returns:
    - None

    Side Effects:
    
    - Generates a chessboard plot of the position of queens on the board.
    
    """
    n = board_bin.shape[0]
    # Create a chessboard pattern with alternating black and white squares
    chessboard = np.zeros((n, n, 3))
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                chessboard[i][j] = [1, 1, 1] # white square
            else:
                chessboard[i][j] = [0, 0, 0] # black square
    # Plot the chessboard
    plt.figure(figsize=(n,n))
    plt.imshow(chessboard)
    for i in range(n):
        for j in range(n):
            if board_bin[i][j] == 1:
                plt.plot(j, i, 'o', markersize=20, markerfacecolor='red', markeredgecolor='black')
    plt.axis('off')
    plt.show()
    
    
def plot_f_pop(f_pop):
    
    """
    Function: plot_f_pop(f_pop)
    --------------------------------------
    This function takes a list of fitness values (f_pop) for a population and creates a scatter plot 
    of the fitness values for each individual in the population.

    Parameters:
    - f_pop (list): A list of fitness values for each individual in the population.

    Returns:
    - None

    Output:
    - A scatter plot of fitness values for each individual in the population, with the x-axis representing 
      the index of each individual in the population and the y-axis representing the fitness value.

    Example:
    >>> f_pop = [5, 3, 8, 9, 2, 7]
    >>> plot_f_pop(f_pop)
    The above example will plot the fitness values of each individual in the population f_pop.
    """
    
    plt.figure()
    plt.title("Fitness der aktuellen Generation")
    plt.scatter(np.arange(len(f_pop)),f_pop, color='k', marker='s')
    plt.ylabel("Fitness")
    plt.xlabel("Individuum")
    plt.tight_layout()
    plt.show()