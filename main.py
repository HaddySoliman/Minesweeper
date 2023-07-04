import numpy as np
import termtables as tt
from Welcome import welcomeInstructions

welcomeInstructions()
global grid 
grid = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])

grid_arr = np.array(grid).reshape(-1, 8)

grid_arr
grid = tt.to_string(
    grid_arr,
    style=tt.styles.ascii_thin,
    # alignment="ll",
    # padding=(0, 1),
)
print(grid)

def checkForBombs():
    for row in range (1, 8):
        for col in range (1, 8):  
            # Check up  
            if row > 0 and grid[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check down    
            if r < n-1  and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check left
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check right
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-left    
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-right
            if r > 0 and col < n-1 and numbers[r-1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-left  
            if r < n-1 and col > 0 and numbers[r+1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-right
            if r < n-1 and col < n-1 and numbers[r+1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1


