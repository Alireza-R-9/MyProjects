#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

// Function to randomly fill the chamber with bullets
vector<bool> fillChamber(int chamberSize, int bulletCount) {
    vector<bool> chamber(chamberSize, false);
    for (int i = 0; i < bulletCount; ++i) {
        int pos;
        do {
            pos = rand() % chamberSize;
        } while (chamber[pos]); // Ensure no duplicate positions
        chamber[pos] = true;
    }
    return chamber;
}

int main() {
    srand(time(0)); // Seed for randomness

    int playerCount, chamberSize = 6, bulletCount;
    vector<string> players;

    // Input the number of players
    cout << "Enter the number of players: ";
    cin >> playerCount;
    cin.ignore(); // Ignore newline character

    if (playerCount < 2) {
        cout << "There must be at least 2 players to play!" << endl;
        return 1;
    }

    // Input player names
    cout << "Enter the names of the players:" << endl;
    for (int i = 0; i < playerCount; ++i) {
        string name;
        cout << "Player " << i + 1 << ": ";
        getline(cin, name);
        players.push_back(name);
    }

    // Input the number of bullets
    cout << "Enter the number of bullets: ";
    cin >> bulletCount;

    if (bulletCount <= 0 || bulletCount >= chamberSize) {
        cout << "Invalid number of bullets. Must be between 1 and " << chamberSize - 1 << "." << endl;
        return 1;
    }

    // Fill the chamber randomly
    vector<bool> chamber = fillChamber(chamberSize, bulletCount);

    // Shuffle players into a queue
    queue<string> playerQueue;
    for (const string& player : players) {
        playerQueue.push(player);
    }

    // Game loop
    int currentChamber = 0;
    while (playerQueue.size() > 1) {
        string currentPlayer = playerQueue.front();
        playerQueue.pop();

        cout << currentPlayer << " pulls the trigger... ";
        if (chamber[currentChamber]) {
            cout << "BANG! " << currentPlayer << " is eliminated!" << endl;
        } else {
            cout << "Click. " << currentPlayer << " survives." << endl;
            playerQueue.push(currentPlayer); // Add the player back to the queue
        }

        currentChamber = (currentChamber + 1) % chamberSize; // Rotate the chamber
    }

    // Announce the winner
    cout << "The winner is: " << playerQueue.front() << "!" << endl;

    return 0;
}
