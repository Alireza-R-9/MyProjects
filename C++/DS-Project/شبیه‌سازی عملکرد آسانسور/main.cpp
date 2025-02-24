#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Request {
    int floor;
    string direction; // "up" or "down"

    Request(int f, string d) : floor(f), direction(d) {}
};

class Elevator {
private:
    int currentFloor;
    string direction; // "up" or "down"
    int totalFloors;
    set<int> upRequests;
    set<int> downRequests;

public:
    Elevator(int floors) : totalFloors(floors), currentFloor(0), direction("up") {}

    void addRequest(int floor, string dir) {
        if (dir == "up") {
            upRequests.insert(floor);
        } else if (dir == "down") {
            downRequests.insert(floor);
        }
    }

    void move() {
        while (!upRequests.empty() || !downRequests.empty()) {
            if (direction == "up") {
                auto it = upRequests.lower_bound(currentFloor);
                if (it != upRequests.end()) {
                    currentFloor = *it;
                    upRequests.erase(it);
                    cout << "Elevator moved to floor " << currentFloor << " (going up)\n";
                } else {
                    direction = "down";
                    cout << "Switching direction to down\n";
                }
            } else if (direction == "down") {
                auto it = downRequests.upper_bound(currentFloor);
                if (it != downRequests.begin()) {
                    --it;
                    currentFloor = *it;
                    downRequests.erase(it);
                    cout << "Elevator moved to floor " << currentFloor << " (going down)\n";
                } else {
                    direction = "up";
                    cout << "Switching direction to up\n";
                }
            }
        }
        cout << "All requests completed. Elevator is idle at floor " << currentFloor << ".\n";
    }

    void displayStatus() const {
        cout << "Current floor: " << currentFloor << "\n";
        cout << "Direction: " << direction << "\n";
        cout << "Up requests: ";
        for (int floor : upRequests) cout << floor << " ";
        cout << "\n";
        cout << "Down requests: ";
        for (int floor : downRequests) cout << floor << " ";
        cout << "\n";
    }
};

int main() {
    int totalFloors;
    cout << "Enter the number of floors in the building: ";
    cin >> totalFloors;

    Elevator elevator(totalFloors);

    int choice;
    do {
        cout << "\n1. Add request\n2. Display status\n3. Move elevator\n4. Exit\nChoose an option: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int floor;
                string direction;
                cout << "Enter the floor number: ";
                cin >> floor;
                cout << "Enter the direction (up/down): ";
                cin >> direction;
                if (floor >= 0 && floor < totalFloors && (direction == "up" || direction == "down")) {
                    elevator.addRequest(floor, direction);
                } else {
                    cout << "Invalid floor or direction. Try again.\n";
                }
                break;
            }
            case 2:
                elevator.displayStatus();
                break;
            case 3:
                elevator.move();
                break;
            case 4:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid option. Try again.\n";
        }
    } while (choice != 4);

    return 0;
}