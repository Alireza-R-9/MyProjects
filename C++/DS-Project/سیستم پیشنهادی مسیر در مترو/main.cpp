#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>

using namespace std;

struct Edge {
    string destination;
    int weight; // time or distance
};

class MetroSystem {
private:
    unordered_map<string, vector<Edge>> graph;

public:
    void addStation(const string& station) {
        if (graph.find(station) == graph.end()) {
            graph[station] = vector<Edge>();
        }
    }

    void addConnection(const string& from, const string& to, int weight) {
        graph[from].push_back({to, weight});
        graph[to].push_back({from, weight}); // Undirected graph
    }

    vector<string> findShortestPath(const string& start, const string& end) {
        unordered_map<string, int> distances;
        unordered_map<string, string> previous;
        priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> pq;

        for (const auto& station : graph) {
            distances[station.first] = numeric_limits<int>::max();
        }

        distances[start] = 0;
        pq.push({0, start});

        while (!pq.empty()) {
            auto [currentDistance, currentStation] = pq.top();
            pq.pop();

            if (currentStation == end) break;

            for (const auto& neighbor : graph[currentStation]) {
                int newDist = currentDistance + neighbor.weight;
                if (newDist < distances[neighbor.destination]) {
                    distances[neighbor.destination] = newDist;
                    previous[neighbor.destination] = currentStation;
                    pq.push({newDist, neighbor.destination});
                }
            }
        }

        vector<string> path;
        for (string at = end; at != ""; at = previous[at]) {
            path.push_back(at);
        }
        reverse(path.begin(), path.end());
        return path;
    }
};

int main() {
    MetroSystem metro;
    metro.addStation("A");
    metro.addStation("B");
    metro.addStation("C");
    metro.addStation("D");

    metro.addConnection("A", "B", 5);
    metro.addConnection("B", "C", 10);
    metro.addConnection("C", "D", 3);
    metro.addConnection("A", "D", 15);

    string start = "A", end = "D";
    vector<string> path = metro.findShortestPath(start, end);

    cout << "Shortest path from " << start << " to " << end << ": ";
    for (const string& station : path) {
        cout << station << " ";
    }
    cout << endl;

    return 0;
}
