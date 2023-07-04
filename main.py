import numpy as np
import termtables as tt


puzzle = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])

puzzle_arr = np.array(puzzle).reshape(-1, 8)

puzzle_arr
grid = tt.to_string(
    puzzle_arr,
    style=tt.styles.ascii_thin,
    # alignment="ll",
    # padding=(0, 1),
)
print(grid)