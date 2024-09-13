import tkinter as tk

# Function to handle a player's move on the grid
def set_tile(row, column):
    global curr_player, game_over

    # Prevent further moves if game is over or tile is already taken
    if game_over or board[row][column]["text"] != "":
        return
    
    # Set the clicked tile with the current player's symbol
    board[row][column]["text"] = curr_player

    # Toggle to the other player (if X, switch to O, and vice versa)
    curr_player = playerO if curr_player == playerX else playerX
    
    # Update the label to display whose turn it is
    label.config(text=f"{curr_player}'s turn")

    # Check if there's a winner or tie after the move
    check_winner()

# Function to check if there is a winner or a tie
def check_winner():
    global turns, game_over
    turns += 1  # Increment turn count with each move

    # List of all possible winning combinations (rows, columns, diagonals)
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # Row 1
        [(1, 0), (1, 1), (1, 2)],  # Row 2
        [(2, 0), (2, 1), (2, 2)],  # Row 3
        [(0, 0), (1, 0), (2, 0)],  # Column 1
        [(0, 1), (1, 1), (2, 1)],  # Column 2
        [(0, 2), (1, 2), (2, 2)],  # Column 3
        [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right to bottom-left
    ]

    # Loop through all winning combinations to check if any player has won
    for combination in winning_combinations:
        if all(board[row][col]["text"] == board[combination[0][0]][combination[0][1]]["text"] != "" for row, col in combination):
            winner = board[combination[0][0]][combination[0][1]]["text"]
            # Display the winner and highlight the winning tiles
            label.config(text=f"{winner} is the winner!", foreground=color_yellow)
            for row, col in combination:
                board[row][col].config(foreground=color_yellow, background=color_light_gray)
            game_over = True  # Mark game as over
            return

    # If 9 turns have passed and no winner, it's a tie
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

# Function to start a new game (reset everything)
def new_game():
    global turns, game_over, curr_player
    turns = 0  # Reset turn count
    game_over = False  # Reset game over flag
    curr_player = playerX  # Reset starting player to X
    label.config(text=f"{curr_player}'s turn", foreground="white")  # Reset label

    # Reset all tiles on the board to empty and default colors
    for row in range(3):
        for col in range(3):
            board[row][col].config(text="", foreground=color_blue, background=color_gray)

# Initialize game settings
playerX, playerO = "X", "O"  # Symbols for the players
curr_player = playerX  # Starting player is X
turns = 0  # Count of turns played
game_over = False  # Flag to check if the game is over

# Define color constants for the game interface
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#1a1919"
color_light_gray = "#646464"

# Setup the main game window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)  # Disable window resizing

# Frame to hold the game board and other UI elements
frame = tk.Frame(window)

# Label to display the current player's turn or the result
label = tk.Label(frame, text=f"{curr_player}'s turn", font=("Consolas", 20),
                 background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")  # Spanning the label across the top

# Create the 3x3 grid of buttons (each representing a tile)
board = [[tk.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_gray, foreground=color_blue,
                    width=4, height=2, command=lambda r=row, c=col: set_tile(r, c))
          for col in range(3)] for row in range(3)]

# Place the buttons in the grid
for row in range(3):
    for col in range(3):
        board[row][col].grid(row=row+1, column=col)

# Button to restart the game
restart_button = tk.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray,
                           foreground="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")  # Placed below the grid

frame.pack()  # Add the frame to the window

# Center the window on the screen
window.update()
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{int((window.winfo_screenwidth() - window.winfo_width()) / 2)}+{int((window.winfo_screenheight() - window.winfo_height()) / 2)}")

# Start the Tkinter event loop (run the game)
window.mainloop()


#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
