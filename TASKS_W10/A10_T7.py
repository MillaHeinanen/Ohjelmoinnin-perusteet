########################################################
# Task A10_T7
# Milla Heinänen
# Date 2025-12-08
########################################################
import random

random.seed(1234)


def layMines(PMineField: list[list[int]], PMines: int) -> None:

    if not PMineField or not isinstance(PMineField, list):
        raise ValueError("PMineField must be a non-empty 2D list.")

    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    if rows == 0 or cols == 0:
        raise ValueError("PMineField must have positive dimensions.")

    capacity = rows * cols
    if PMines < 0 or PMines > capacity:
        raise ValueError(f"PMines must be between 0 and {capacity}.")

    all_positions = list(range(capacity))
    mine_positions = random.sample(all_positions, PMines)

    for pos in mine_positions:
        r = pos // cols
        c = pos % cols
        PMineField[r][c] = 9
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] != 9:
                PMineField[r][c] = 0
    return None


def calculateNearbys(PMineField: list[list[int]]) -> None:
    if not PMineField or not isinstance(PMineField, list):
        raise ValueError("PMineField must be a non-empty 2D list.")

    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    if rows == 0 or cols == 0:
        raise ValueError("PMineField must have positive dimensions.")

    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                # Keep mines as 9
                continue
            count = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count

    return None


def generateMinefield(
    PMineField: list[list[int]],
    PRows: int,
    PCols: int,
    PMines: int
) -> None:

    if PRows <= 0 or PCols <= 0:
        raise ValueError("PRows and PCols must be positive integers.")

    capacity = PRows * PCols
    if PMines < 0 or PMines > capacity:
        raise ValueError(f"PMines must be between 0 and {capacity}.")

    PMineField.clear()
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)

    layMines(PMineField, PMines)

    calculateNearbys(PMineField)

    return None

def _print_menu() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")


def _show_board(board: list[list[int]]) -> None:
    if not board:
        print("No board generated yet. Choose option 1 first.")
        return
    for row in board:
        print(row)


def _save_board(board: list[list[int]]) -> None:
    if not board:
        print("No board generated yet. Choose option 1 first.")
        return
    filename = input("Insert filename: ").strip()


def main() -> None:
    print("Program starting.")

    board: list[list[int]] = []

    while True:
        print()
        _print_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            try:
                rows = int(input("Insert rows: ").strip())
                cols = int(input("Insert columns: ").strip())
                mines = int(input("Insert mines: ").strip())
                generateMinefield(board, rows, cols, mines)
            except ValueError as ve:
                print(f"Error: {ve}")
                # Keep looping

        elif choice == "2":
            _show_board(board)

        elif choice == "3":
            _save_board(board)

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()