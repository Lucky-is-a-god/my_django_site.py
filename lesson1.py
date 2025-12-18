def print_board(board):
    """Печатает игровое поле в консоли."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Проверяет, есть ли победитель."""
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]  # Возвращает 'X' или 'O'

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Если нет победителя
    return None

def is_board_full(board):
    """Проверяет, заполнено ли поле (ничья)."""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board, current_player):
    """Получает ход от игрока и проверяет его корректность."""
    while True:
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (1-3): ")) - 1
            col = int(input(f"Игрок {current_player}, введите номер столбца (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректные координаты. Введите числа от 1 до 3.")
        except ValueError:
            print("Ошибка! Введите числа.")

def main():
    """Основная функция игры."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Добро пожаловать в игру 'Крестики-нолики'!")
    print("Для хода вводите номера строки и столбца (от 1 до 3).")

    while True:
        print_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Игрок {winner} победил! 🎉")
            break

        if is_board_full(board):
            print_board(board)
            print("Ничья! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

if name == "__main__":
    main()