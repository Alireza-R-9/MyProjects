#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

// Function to find the largest rectangle in a histogram
int largestRectangleInHistogram(vector<int>& heights) {
    stack<int> s;
    int maxArea = 0;
    int n = heights.size();

    for (int i = 0; i <= n; ++i) {
        int h = (i == n) ? 0 : heights[i];
        while (!s.empty() && h < heights[s.top()]) {
            int height = heights[s.top()];
            s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        s.push(i);
    }

    return maxArea;
}

// Function to find the largest rectangle of 1s in a binary matrix
int maximalRectangle(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;

    int m = matrix.size();
    int n = matrix[0].size();
    vector<int> heights(n, 0);
    int maxArea = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            heights[j] = (matrix[i][j] == 0) ? 0 : heights[j] + 1;
        }
        maxArea = max(maxArea, largestRectangleInHistogram(heights));
    }

    return maxArea;
}

int main() {
    int rows, cols;
    cout << "Enter the number of rows and columns: ";
    cin >> rows >> cols;

    vector<vector<int>> matrix(rows, vector<int>(cols));
    cout << "Enter the binary matrix (0s and 1s):\n";
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cin >> matrix[i][j];
        }
    }

    int result = maximalRectangle(matrix);
    cout << "The area of the largest rectangle is: " << result << endl;

    return 0;
}
