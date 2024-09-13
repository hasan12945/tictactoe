import tkinter as tk

def set_tile(row, column):
    global curr_player, game_over

    if game_over or board[row][column]["text"] != "":
        return  # Return if game is over or tile is already taken
    
    board[row][column]["text"] = curr_player  # Set tile with current player symbol
    curr_player = playerO if curr_player == playerX else playerX  # Toggle player
    label.config(text=f"{curr_player}'s turn")  # Update label

    check_winner()  # Check for a winner

def check_winner():
    global turns, game_over
    turns += 1
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # Rows
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  # Columns
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # Diagonals
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combination in winning_combinations:
        if all(board[row][col]["text"] == board[combination[0][0]][combination[0][1]]["text"] != "" for row, col in combination):
            winner = board[combination[0][0]][combination[0][1]]["text"]
            label.config(text=f"{winner} is the winner!", foreground=color_yellow)
            for row, col in combination:
                board[row][col].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    if turns == 9:  # If 9 turns have passed and no winner, it's a tie
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=f"{curr_player}'s turn", foreground="white")

    for row in range(3):
        for col in range(3):
            board[row][col].config(text="", foreground=color_blue, background=color_gray)

# Game setup
playerX, playerO = "X", "O"
curr_player = playerX
turns = 0
game_over = False
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#1a1919"
color_light_gray = "#646464"

# Window setup
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=f"{curr_player}'s turn", font=("Consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Create the 3x3 grid of buttons
board = [[tk.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_gray, foreground=color_blue,
                    width=4, height=2, command=lambda r=row, c=col: set_tile(r, c))
          for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        board[row][col].grid(row=row+1, column=col)

# Restart button
restart_button = tk.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray, foreground="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window
window.update()
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{int((window.winfo_screenwidth() - window.winfo_width()) / 2)}+{int((window.winfo_screenheight() - window.winfo_height()) / 2)}")

window.mainloop()


#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
