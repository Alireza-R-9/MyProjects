#include <iostream>
#include <vector>
using namespace std;

#define N 8

// Function to print the chessboard
void printSolution(const vector<vector<int>>& board) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// Function to check if a queen can be placed at board[row][col]
bool isSafe(const vector<vector<int>>& board, int row, int col) {
    // Check this row on the left side
    for (int i = 0; i < col; i++) {
        if (board[row][i]) return false;
    }

    // Check upper diagonal on the left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j]) return false;
    }

    // Check lower diagonal on the left side
    for (int i = row, j = col; i < N && j >= 0; i++, j--) {
        if (board[i][j]) return false;
    }

    return true;
}

// Recursive function to solve the N-Queens problem
bool solveNQueensUtil(vector<vector<int>>& board, int col, vector<vector<vector<int>>>& solutions) {
    // Base case: If all queens are placed, save the solution
    if (col >= N) {
        solutions.push_back(board);
        return true;
    }

    bool res = false;

    // Consider this column and try placing a queen in all rows one by one
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            // Place the queen
            board[i][col] = 1;

            // Recur to place the rest of the queens
            res = solveNQueensUtil(board, col + 1, solutions) || res;

            // Backtrack: Remove the queen
            board[i][col] = 0;
        }
    }

    return res;
}

// Function to solve the N-Queens problem
void solveNQueens() {
    vector<vector<int>> board(N, vector<int>(N, 0));
    vector<vector<vector<int>>> solutions;

    solveNQueensUtil(board, 0, solutions);

    // Print all solutions
    cout << "Total solutions: " << solutions.size() << endl;
    for (const auto& solution : solutions) {
        printSolution(solution);
    }
}

int main() {
    cout << "Solutions to the 8-Queens problem:\n";
    solveNQueens();
    return 0;
}
