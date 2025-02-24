#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class SocialNetwork {
private:
    unordered_map<string, vector<string>> graph; // Adjacency list to store connections
    bool isDirected;

public:
    // Constructor to initialize the graph type (directed or undirected)
    SocialNetwork(bool directed = false) : isDirected(directed) {}

    // Add a connection between two people
    void addConnection(const string &person1, const string &person2) {
        graph[person1].push_back(person2);
        if (!isDirected) {
            graph[person2].push_back(person1);
        }
    }

    // Display the connections in the network
    void displayConnections() {
        for (const auto &entry : graph) {
            cout << entry.first << " is connected to: ";
            for (const auto &connection : entry.second) {
                cout << connection << " ";
            }
            cout << endl;
        }
    }

    // Calculate the degree of each person
    void calculateDegrees() {
        unordered_map<string, int> degrees;
        for (const auto &entry : graph) {
            degrees[entry.first] = entry.second.size();
        }

        // Display degrees
        cout << "\nDegrees of each person:\n";
        for (const auto &entry : degrees) {
            cout << entry.first << ": " << entry.second << " connections\n";
        }

        // Find the person with the highest degree
        auto maxElement = max_element(degrees.begin(), degrees.end(), [](const auto &a, const auto &b) {
            return a.second < b.second;
        });

        cout << "\nPerson with the most connections: " << maxElement->first << " (" << maxElement->second << " connections)\n";
    }
};

int main() {
    cout << "Social Network Analysis\n";

    int numConnections;
    bool isDirected;

    // Ask if the graph is directed or undirected
    cout << "Is the network directed? (1 for Yes, 0 for No): ";
    cin >> isDirected;

    // Create the social network
    SocialNetwork network(isDirected);

    // Input the number of connections
    cout << "Enter the number of connections: ";
    cin >> numConnections;

    cout << "Enter the connections (Format: Person1 Person2):\n";
    for (int i = 0; i < numConnections; ++i) {
        string person1, person2;
        cin >> person1 >> person2;
        network.addConnection(person1, person2);
    }

    // Display the connections and analyze the network
    cout << "\nConnections in the network:\n";
    network.displayConnections();

    network.calculateDegrees();

    return 0;
}