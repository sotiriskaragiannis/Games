#include <stdio.h>
#include <stdbool.h>

#define N 9
#define UNASSIGNED 0

void printGrid(int grid[N][N]);
bool findEmptyPlace(int grid[N][N], int *row, int *col);
bool isSafe(int grid[N][N], int row, int col, int num);
bool usedInRow(int grid[N][N], int row, int num);
bool usedInCol(int grid[N][N], int col, int num);
bool usedInBlock(int grid[N][N], int row, int col, int num);
bool solveSudoku(int grid[N][N]);

int main(){

   int row, col;
    // assigning values to the grid.
    int grid[N][N] ={{8, 0, 0, 0, 0, 0, 0, 0, 0},
                     {0, 0, 3, 6, 0, 0, 0, 0, 0},
                     {0, 7, 0, 0, 9, 0, 2, 0, 0},
                     {0, 5, 0, 0, 0, 7, 0, 0, 0},
                     {0, 0, 0, 0, 4, 5, 7, 0, 0},
                     {0, 0, 0, 1, 0, 0, 0, 3, 0},
                     {0, 0, 1, 0, 0, 0, 0, 6, 8},
                     {0, 0, 8, 5, 0, 0, 0, 1, 0},
                     {0, 9, 0, 0, 0, 0, 4, 0, 0}};
    printf("Before: \n");
    printGrid(grid);

    printf("After: \n");
    if (solveSudoku(grid) == true)
        printGrid(grid);
    else
        printf("No solution exists\n");
    return 0;
}


// A function to display the grid in a beautiful way.
void printGrid(int grid[N][N]){

    printf("+-----------------------+\n");
    for (int row = 0; row < N; row++) {
        printf("|");
        for (int col = 0; col < N; col++){
            if (grid[row][col] == 0){
                printf("  ");
            } else {
                printf("%2d", grid[row][col]);
            }
            if ((col+1) % 3 ==0){
                printf(" |");
            }
        }
        if ((row+1) % 3 ==0){
                printf("\n+-----------------------+");
            }
        printf("\n");
    }
}

bool solveSudoku(int grid[N][N]){
    int row, col;

    // If there are no empty blocks mark success.
    if (!findEmptyPlace(grid, &row, &col)){
        return true;
    }

    // For digits 1 to 9
    for (int num = 1; num <= 9; num++)
    {
         
        // Check if looks promising
        if (isSafe(grid, row, col, num))
        {
             
            // Make tentative assignment
            grid[row][col] = num;

            // Return, if success.
            if (solveSudoku(grid))
                return true;
 
            // Failure, unmake & try again with the next promising digit.
            grid[row][col] = UNASSIGNED;
        }
    }
   
    // This triggers backtracking.
    return false;
}

// Searches the grid to find an entry that is still unassigned.
bool findEmptyPlace(int grid[N][N], int *row, int *col){

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (grid[i][j] == UNASSIGNED){
                *row = i;
                *col = j;
                return true;
            }  
        }
    }
}

// Checks if a number can be put in an empty place.
bool isSafe(int grid[N][N], int row, int col, int num){
    return !usedInBlock(grid, row, col, num) && !usedInCol(grid, col, num) && !usedInRow(grid, row, num);
}

// Checks if a number is used in a row.
bool usedInRow(int grid[N][N], int row, int num){

    for (int i = 0; i < N; i++){
        if (grid[row][i] == num){
            return true;
        }
    }
    return false;
}

// Checks if a number is used in a column.
bool usedInCol(int grid[N][N], int col, int num){
    
    for (int i = 0; i < N; i++){
        if (grid[i][col] == num){
            return true;
        }
    }
    return false;
}

// Checks if a number is used in a 3x3 block.
bool usedInBlock(int grid[N][N], int row, int col, int num){
    
    int block_start_row = row - row % 3;
    int block_start_col = col - col % 3;

    for (int i = block_start_row; i < block_start_row + 3; i++){
        for (int j = block_start_col; j < block_start_col + 3; j++){
            if (grid[i][j] == num){
                return true;
            }
        }
    }
    return false;
}
