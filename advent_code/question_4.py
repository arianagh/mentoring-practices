def load_grid(file_path: str):
    """
    Reads the grid from a text file.
    Each line in the file represents a row in the grid.
    """
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def count_word_in_grid(grid, word):
    """Count the number of times the word appears in the grid in all directions."""
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Down-Right (Diagonal)
        (1, -1),  # Down-Left (Diagonal)
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1),  # Up-Left (Diagonal)
        (-1, 1),  # Up-Right (Diagonal)
    ]
    count = 0

    def is_word_at(x, y, dx, dy):
        """Check if the word exists starting from (x, y) in direction (dx, dy)."""
        for k in range(word_length):
            nx, ny = x + k * dx, y + k * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[k]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_word_at(x, y, dx, dy):
                    count += 1
    return count


if __name__ == "__main__":
    # File path to the grid
    file_path = "question_4.txt"  # Replace with your file path

    # Load the grid from the file
    grid = load_grid(file_path)

    # Define the word to search for
    word = "XMAS"

    # Count occurrences of the word in the grid
    result = count_word_in_grid(grid, word)
    print(f"Total occurrences of '{word}': {result}")
