#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;

// Function to print the status of rods
void printRods(const vector<stack<int>>& rods, int numDisks) {
    cout << "Current state of rods:\n";
    for (int i = 0; i < 3; ++i) {
        cout << "Rod " << char('A' + i) << ": ";
        stack<int> temp = rods[i]; // Copy the stack to print its content
        vector<int> rodContents;
        while (!temp.empty()) {
            rodContents.push_back(temp.top());
            temp.pop();
        }
        for (auto it = rodContents.rbegin(); it != rodContents.rend(); ++it) {
            cout << *it << " ";
        }
        cout << endl;
    }
    cout << "-----------------------------\n";
}

// Function to move a disk between two rods
void moveDisk(vector<stack<int>>& rods, int from, int to) {
    if (rods[from].empty()) {
        throw invalid_argument("Invalid move: Source rod is empty.");
    }
    if (!rods[to].empty() && rods[from].top() > rods[to].top()) {
        throw invalid_argument("Invalid move: Cannot place a larger disk on a smaller one.");
    }
    int disk = rods[from].top();
    rods[from].pop();
    rods[to].push(disk);
    cout << "Move disk " << disk << " from rod " << char('A' + from)
         << " to rod " << char('A' + to) << endl;
    printRods(rods, rods[0].size() + rods[1].size() + rods[2].size());
}

// Recursive function to solve Tower of Hanoi
void solveHanoi(vector<stack<int>>& rods, int n, int from, int to, int aux) {
    if (n == 1) {
        moveDisk(rods, from, to);
        return;
    }
    solveHanoi(rods, n - 1, from, aux, to);
    moveDisk(rods, from, to);
    solveHanoi(rods, n - 1, aux, to, from);
}

int main() {
    int numDisks;

    cout << "Tower of Hanoi Solver (using stacks)\n";
    cout << "Enter the number of disks: ";
    cin >> numDisks;

    if (numDisks <= 0) {
        cerr << "Number of disks must be greater than zero.\n";
        return 1;
    }

    // Initialize the rods
    vector<stack<int>> rods(3); // rods[0]: A, rods[1]: B, rods[2]: C

    // Add disks to the first rod (A)
    for (int i = numDisks; i >= 1; --i) {
        rods[0].push(i);
    }

    cout << "Initial state of rods:\n";
    printRods(rods, numDisks);

    // Solve the Tower of Hanoi
    try {
        solveHanoi(rods, numDisks, 0, 2, 1); // From A to C using B as auxiliary
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }

    cout << "All disks successfully moved to rod C.\n";
    return 0;
}
