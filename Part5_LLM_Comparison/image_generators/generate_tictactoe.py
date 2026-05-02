import matplotlib.pyplot as plt


def parse_board(board_state):
    """Convert board string into a list of cells"""
    return board_state.split('|')


def draw_board(board_state):
    """Draw a tic tac toe board from a board state string"""
    board = parse_board(board_state)

    fig, ax = plt.subplots(figsize=(4, 4))

    # draw grid
    for i in range(1, 3):
        ax.plot([0, 3], [i, i], color='black')
        ax.plot([i, i], [0, 3], color='black')

    # place symbols
    for i, cell in enumerate(board):
        row = 2 - (i // 3)
        col = i % 3

        if cell == 'X':
            ax.text(
                col + 0.5, row + 0.5, 'X',
                fontsize=40, ha='center', va='center', color='red'
            )
        elif cell == 'O':
            ax.text(
                col + 0.5, row + 0.5, 'O',
                fontsize=40, ha='center', va='center', color='blue'
            )

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.axis('off')

    return fig


def save_single_board():
    """Generate and save one test board"""
    board = "X|_|_|_|X|_|_|_|O"

    fig = draw_board(board)
    fig.savefig("board.png", bbox_inches='tight')

    print("Saved board.png")
    plt.show()


def save_multiple_boards():
    """Generate and save multiple boards for testing"""
    boards = [
        "X|_|_|_|X|_|_|_|O",
        "X|O|_|_|X|_|_|_|O",
        "_|X|_|O|_|_|_|_|X",
        "X|X|X|_|_|_|_|_|_",
        "_|_|_|O|O|O|_|_|_",
        "X|_|_|_|O|_|_|_|X",
        "_|_|O|_|X|_|O|_|_",
        "_|X|_|_|_|_|_|O|_"
    ]

    for i, board in enumerate(boards):
        fig = draw_board(board)
        fig.savefig(f"ttt_{i}.png", bbox_inches='tight')

    print(f"Saved {len(boards)} boards")

if __name__ == "__main__":
    save_single_board()
    save_multiple_boards()
