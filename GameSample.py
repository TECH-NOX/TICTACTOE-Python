from builtins import print
import itertools


def display_game(game):
    print("   0"," 1"," 2")
    for col, row in enumerate(game):
        print(col,row)
    print()


def play(player_input):
    try:
        row_idx = int(input("Which row you would like to alter? ( 0 , 1 , 2 ) - "))
        col_idx = int(input("Which column you would like to alter? ( 0 , 1 , 2 ) - "))
        game[row_idx][col_idx] = player_input
    except IndexError as e:
        print("OOPS !! Sorry that is an invalid entry \n"
              "Make Sure to provide values with in range ( 0 / 1 / 2 )\n"
              "Error Thrown => ",e)


def check_winner(game):
    for each_row in game:
        if each_row.count(each_row[0]) == len(each_row) and each_row[0] != 0:
            print("Winner - Horizantally matched")
            return True

    for column in range(len(game)):
        vertical_list = []
        for row_list in game:
            vertical_list.append(row_list[column])
        if vertical_list.count(vertical_list[0]) == len(vertical_list) and vertical_list[0] != 0:
            print("Winner - Vertically Matched")
            return True

# game[0][0] == game [1][1] == game[2][2]
    left_top_right_bottom_diag_list = []
    for idx in range(len(game)):
        left_top_right_bottom_diag_list.append(game[idx][idx])
    if left_top_right_bottom_diag_list.count(left_top_right_bottom_diag_list[0]) == len(left_top_right_bottom_diag_list) and left_top_right_bottom_diag_list[0] != 0:
        print("Winner - Diagonally from Left Top to Right Bottom Matched")
        return True

# game[2][0] == game [1][1] == game[0][2]
    right_bottom_left_top_diag_list = []
    for row, col in enumerate(reversed(range(len(game)))):
        right_bottom_left_top_diag_list.append(game[row][col])
    if right_bottom_left_top_diag_list.count(right_bottom_left_top_diag_list[0]) == len(right_bottom_left_top_diag_list) and right_bottom_left_top_diag_list[0] != 0:
        print("Winner - Diagonally from Right Bottom to Left Top Matched")
        return True
    return False


# game_play = True
players = [1,2]


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

display_game(game)
game_won = False
player_shift = itertools.cycle(players)

while not game_won:
    current_player = next(player_shift)
    print(f" Player {current_player}'s move")
    play(current_player)
    display_game(game)
    if check_winner(game):
        game_won = True
