def draw_board(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == " ":
                if y < len(board) - 1:
                    print(board[x][y], "| ", end='')
                else:
                    print(board[x][y], "| ")
            elif board[x][y] == "X":
                if y < len(board) - 1:
                    print('X', "| ", end='')
                else:
                    print('X', "| ")
            elif board[x][y] == "0":
                if y < len(board) - 1:
                    print('0', "| ", end='')
                else:
                    print('0', "| ")
        print("-----------")


def check_win(player, board):
    for i in range(len(board)):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def ask_move(player, board):
    while True:
        try:
            x, y = input(f"{player}, Введите x и y координаты: ").strip().split()
            x, y = int(x), int(y)
            if 0 <= x <= len(board) and 0 <= y <= len(board):
                if board[y][x] == " ":
                    board[y][x] = player
                    break
                else:
                    draw_board(board)
                    print('Эта клетка занята')
                    ask_move(player, board)
                    break
            else:
                print('Вне диапозона')
        except ValueError:
            print('Неккоректный ввод')


def tic_tac_toe():
    board = [[' ' for i in range(3)] for j in range(3)]
    player = 'X'
    draw_board(board)

    while True:
        ask_move(player, board)
        draw_board(board)
        if check_win(player, board):
            print(f'Игрок: {player} Победил!')
            break

        if all(cell != " " for row in board for cell in row):
            print("Ничья!")
            break

        player = "0" if player == "X" else "X"

    while True:
        try:
            restart = int(input('Хотите сыграть еще раз?(0: Нет, 1: Да)'))
            if restart == 1:
                tic_tac_toe()
            elif restart == 0:
                break
        except ValueError:
            print('Неккоректный ввод!')


tic_tac_toe()