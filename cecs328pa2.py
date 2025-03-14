# Name: Nadhirah Michael-Ho
# Filename: cecs328pa2.py
# Description: Converts a line code representation into its NRZ binary encoding.


def nrz_encoding(input: str) -> str:
    # Split the input string by newlines to process line by line
    lines = input.split("\n")
    
    # Determine the maximum width of the lines to normalize them
    width = max([len(line) for line in lines])

    # Initialize a list to hold the normalized grid
    grid = []
    
    # Normalize the input lines by adding spaces to match the maximum width
    for i in range(1, len(lines)-1):
        # Append each normalized line (line with spaces added) to the grid
        grid.append(list(lines[i] + " " * (width - len(lines[i]))))

    # Return an empty string if the grid is empty
    if not grid:
        return ""

    # Get the number of rows (n) and columns (m) in the grid
    n = len(grid)
    m = len(grid[0])

    # Initialize the result string with the first value based on the top-left corner of the grid
    res = ""
    res += ("1" if grid[0][0] == "_" else "0")

    # Initialize the column index (j) to 3 and row index (i) depending on the top-left corner
    j = 3
    i = (0 if grid[0][0] == "_" or " " else n-1)

    # Start the encoding process by traversing the grid
    while j < m:
        # If the current grid position is "_", add "1" and move 3 columns to the right
        if grid[i][j] == "_":
            j += 3
            res += ("1" if i == 0 else "0")

        # If the current grid position is a space, move to the last row and advance one column
        elif grid[i][j] == " ":
            i = n - 1
            j += 1

        # If the current grid position is "|", move to the first row and advance one column
        elif grid[i][j] == "|":
            i = 0
            j += 1

    # Return the final result string
    return res

