#include <iostream>
#include <stack>
#include <queue>
#include <string>

using namespace std;

class BrowserHistory {
private:
    stack<string> backStack;
    stack<string> forwardStack;
    queue<string> downloadQueue;
    string currentPage;

public:
    BrowserHistory() {
        currentPage = "Home";
    }

    void visitPage(const string& url) {
        if (!currentPage.empty()) {
            backStack.push(currentPage);
        }
        currentPage = url;
        while (!forwardStack.empty()) {
            forwardStack.pop();
        }
        cout << "Visiting: " << currentPage << endl;
    }

    void goBack() {
        if (!backStack.empty()) {
            forwardStack.push(currentPage);
            currentPage = backStack.top();
            backStack.pop();
            cout << "Back to: " << currentPage << endl;
        } else {
            cout << "No previous pages!" << endl;
        }
    }

    void goForward() {
        if (!forwardStack.empty()) {
            backStack.push(currentPage);
            currentPage = forwardStack.top();
            forwardStack.pop();
            cout << "Forward to: " << currentPage << endl;
        } else {
            cout << "No forward pages!" << endl;
        }
    }

    void addDownload(const string& file) {
        downloadQueue.push(file);
        cout << "Added to download queue: " << file << endl;
    }

    void processDownload() {
        if (!downloadQueue.empty()) {
            cout << "Downloading: " << downloadQueue.front() << endl;
            downloadQueue.pop();
        } else {
            cout << "No files to download!" << endl;
        }
    }

    void clearHistory() {
        while (!backStack.empty()) backStack.pop();
        while (!forwardStack.empty()) forwardStack.pop();
        cout << "History cleared!" << endl;
    }
};

int main() {
    BrowserHistory browser;
    int choice;
    string input;

    while (true) {
        cout << "\n1. Visit Page\n2. Go Back\n3. Go Forward\n4. Add Download\n5. Process Download\n6. Clear History\n7. Exit\nEnter your choice: ";
        cin >> choice;
        cin.ignore(); // To handle newline character after integer input

        switch (choice) {
            case 1:
                cout << "Enter URL: ";
                getline(cin, input);
                browser.visitPage(input);
                break;
            case 2:
                browser.goBack();
                break;
            case 3:
                browser.goForward();
                break;
            case 4:
                cout << "Enter file name: ";
                getline(cin, input);
                browser.addDownload(input);
                break;
            case 5:
                browser.processDownload();
                break;
            case 6:
                browser.clearHistory();
                break;
            case 7:
                cout << "Exiting..." << endl;
                return 0;
            default:
                cout << "Invalid choice! Try again." << endl;
        }
    }
}
