#include <iostream>
#include <queue>
#include <string>
#include <iomanip>

using namespace std;

// Structure to represent a call
struct Call {
    string name;
    string number;
    string time;
    string type; // "Incoming" or "Outgoing"
};

// Function prototypes
void addCall(queue<Call>& callQueue);
void processNextCall(queue<Call>& callQueue);
void viewCallList(const queue<Call>& callQueue);
void searchCall(const queue<Call>& callQueue);

int main() {
    queue<Call> callQueue;
    int choice;

    do {
        cout << "\nCall Management System" << endl;
        cout << "1. Add new call" << endl;
        cout << "2. Process next call" << endl;
        cout << "3. View call list" << endl;
        cout << "4. Search call" << endl;
        cout << "5. Exit" << endl;
        cout << "Choose an option: ";
        cin >> choice;
        cin.ignore(); // Clear the input buffer

        switch (choice) {
            case 1:
                addCall(callQueue);
                break;
            case 2:
                processNextCall(callQueue);
                break;
            case 3:
                viewCallList(callQueue);
                break;
            case 4:
                searchCall(callQueue);
                break;
            case 5:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 5);

    return 0;
}

void addCall(queue<Call>& callQueue) {
    Call newCall;

    cout << "Enter caller name: ";
    getline(cin, newCall.name);

    cout << "Enter caller number: ";
    getline(cin, newCall.number);

    cout << "Enter call time: ";
    getline(cin, newCall.time);

    cout << "Enter call type (Incoming/Outgoing): ";
    getline(cin, newCall.type);

    callQueue.push(newCall);
    cout << "Call added successfully!" << endl;
}

void processNextCall(queue<Call>& callQueue) {
    if (callQueue.empty()) {
        cout << "No calls in the queue to process." << endl;
    } else {
        Call nextCall = callQueue.front();
        cout << "Processing call:" << endl;
        cout << "Name: " << nextCall.name << endl;
        cout << "Number: " << nextCall.number << endl;
        cout << "Time: " << nextCall.time << endl;
        cout << "Type: " << nextCall.type << endl;
        callQueue.pop();
    }
}

void viewCallList(const queue<Call>& callQueue) {
    if (callQueue.empty()) {
        cout << "No calls in the queue." << endl;
    } else {
        queue<Call> tempQueue = callQueue; // Copy the queue to traverse it
        cout << left << setw(15) << "Name" << setw(15) << "Number" << setw(15) << "Time" << setw(15) << "Type" << endl;
        cout << string(60, '-') << endl;
        while (!tempQueue.empty()) {
            Call call = tempQueue.front();
            cout << left << setw(15) << call.name << setw(15) << call.number << setw(15) << call.time << setw(15) << call.type << endl;
            tempQueue.pop();
        }
    }
}

void searchCall(const queue<Call>& callQueue) {
    if (callQueue.empty()) {
        cout << "No calls in the queue." << endl;
        return;
    }

    string searchTerm;
    cout << "Enter name or number to search: ";
    getline(cin, searchTerm);

    queue<Call> tempQueue = callQueue; // Copy the queue to traverse it
    bool found = false;

    while (!tempQueue.empty()) {
        Call call = tempQueue.front();
        if (call.name == searchTerm || call.number == searchTerm) {
            cout << "Call found:" << endl;
            cout << "Name: " << call.name << endl;
            cout << "Number: " << call.number << endl;
            cout << "Time: " << call.time << endl;
            cout << "Type: " << call.type << endl;
            found = true;
        }
        tempQueue.pop();
    }

    if (!found) {
        cout << "No matching call found." << endl;
    }
}

