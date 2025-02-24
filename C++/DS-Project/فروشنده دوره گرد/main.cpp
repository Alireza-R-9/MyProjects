#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cmath>

using namespace std;

// Function to calculate Euclidean distance between two points
double calculateDistance(pair<int, int> city1, pair<int, int> city2) {
    return sqrt(pow(city1.first - city2.first, 2) + pow(city1.second - city2.second, 2));
}

// Function to solve TSP using Brute Force
pair<vector<int>, double> tspBruteForce(const vector<pair<int, int>>& cities) {
    int n = cities.size();
    vector<int> perm;
    for (int i = 0; i < n; ++i) {
        perm.push_back(i);
    }

    vector<int> optimalPath;
    double minDistance = DBL_MAX;

    do {
        double currentDistance = 0;
        for (int i = 0; i < n - 1; ++i) {
            currentDistance += calculateDistance(cities[perm[i]], cities[perm[i + 1]]);
        }
        currentDistance += calculateDistance(cities[perm[n - 1]], cities[perm[0]]);

        if (currentDistance < minDistance) {
            minDistance = currentDistance;
            optimalPath = perm;
        }
    } while (next_permutation(perm.begin(), perm.end()));

    return {optimalPath, minDistance};
}

// Function to print the path
void printPath(const vector<int>& path, double distance) {
    cout << "Optimal Path: ";
    for (int i = 0; i < path.size(); ++i) {
        cout << path[i] + 1;
        if (i < path.size() - 1) {
            cout << " -> ";
        }
    }
    cout << " -> " << path[0] + 1 << endl;
    cout << "Total Distance: " << distance << endl;
}

int main() {
    int n;
    cout << "Enter the number of cities: ";
    cin >> n;

    vector<pair<int, int>> cities(n);
    cout << "Enter the coordinates of the cities (x y):\n";
    for (int i = 0; i < n; ++i) {
        cout << "City " << i + 1 << ": ";
        cin >> cities[i].first >> cities[i].second;
    }

    pair<vector<int>, double> result = tspBruteForce(cities);
    printPath(result.first, result.second);

    return 0;
}