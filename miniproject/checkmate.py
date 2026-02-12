def checkmate(board):
    # แปลงกระดานเป็น 2 มิติ
    lines = board.strip().split('\n')
    board_size = len(lines)

    grid = []
    for line in lines:
        grid.append(list(line))

    # หา King
    king_row = -1
    king_col = -1

    for row in range(board_size):
        for col in range(board_size):
            if grid[row][col] == 'K':
                king_row = row
                king_col = col


    # ใช้กับ R, B, Q
    def scan(direction_row, direction_col, start_row, start_col):
        current_row = start_row + direction_row
        current_col = start_col + direction_col

        while 0 <= current_row < board_size and 0 <= current_col < board_size:
            if grid[current_row][current_col] != '.':
                return grid[current_row][current_col]

            current_row += direction_row
            current_col += direction_col

        return None

    # ตรวจหมาก
    for row in range(board_size):
        for col in range(board_size):
            piece = grid[row][col]

            # ข้าม . , ข้าม King
            if piece == '.' or piece == 'K':
                continue

            # Pawn (P)
            # โจมตีเฉียงขึ้น 1 ช่อง
            if piece == 'P':
                is_one_row_up = (row - 1 == king_row)
                is_diagonal = (abs(col - king_col) == 1)

                if is_one_row_up and is_diagonal:
                    print("Success")
                    return

            # Rook (R)
            # แนวตรง แถวหรือคอลัมน์เดียวกัน
            if piece == 'R':
                same_row = (row == king_row)
                same_col = (col == king_col)

                if same_row or same_col:
                    if same_row:
                        direction_row = 0
                    else:
                        direction_row = 1 if king_row > row else -1

                    if same_col:
                        direction_col = 0
                    else:
                        direction_col = 1 if king_col > col else -1

                    if scan(direction_row, direction_col, row, col) == 'K':
                        print("Success")
                        return

            # Bishop (B)
            # แนวทแยง
            if piece == 'B':
                diagonal = abs(row - king_row) == abs(col - king_col)

                if diagonal:
                    direction_row = 1 if king_row > row else -1
                    direction_col = 1 if king_col > col else -1

                    if scan(direction_row, direction_col, row, col) == 'K':
                        print("Success")
                        return

            # Queen (Q)
            # แนวตรง หรือ แนวทแยง
            same_row = (row == king_row)
            same_col = (col == king_col)
            diagonal = abs(row - king_row) == abs(col - king_col)

            if piece == 'Q' and (same_row or same_col or diagonal):

                if same_row:
                    direction_row = 0
                else:
                    direction_row = 1 if king_row > row else -1

                if same_col:
                    direction_col = 0
                else:
                    direction_col = 1 if king_col > col else -1

                if scan(direction_row, direction_col, row, col) == 'K':
                    print("Success")
                    return

    # ไม่มีใครโจมตี King
    print("Fail")
