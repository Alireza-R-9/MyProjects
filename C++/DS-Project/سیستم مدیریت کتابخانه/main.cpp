#include <iostream>
#include <string>
#include <fstream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

struct Book {
    int id;
    string title;
    string author;
    int year;
    Book* left;
    Book* right;

    Book(int id, string title, string author, int year)
            : id(id), title(title), author(author), year(year), left(nullptr), right(nullptr) {}
};

class Library {
private:
    Book* root;

    // Helper function to add a book to the BST
    Book* addBookHelper(Book* node, int id, string title, string author, int year) {
        if (!node) {
            return new Book(id, title, author, year);
        }
        if (id < node->id) {
            node->left = addBookHelper(node->left, id, title, author, year);
        } else {
            node->right = addBookHelper(node->right, id, title, author, year);
        }
        return node;
    }

    // Helper function to search for a book by ID
    Book* searchBookHelper(Book* node, int id) {
        if (!node || node->id == id) {
            return node;
        }
        if (id < node->id) {
            return searchBookHelper(node->left, id);
        }
        return searchBookHelper(node->right, id);
    }

    // Helper function to display books in-order
    void inOrderTraversal(Book* node) {
        if (!node) return;
        inOrderTraversal(node->left);
        cout << "ID: " << node->id << ", Title: " << node->title
             << ", Author: " << node->author << ", Year: " << node->year << endl;
        inOrderTraversal(node->right);
    }

    // Helper function to delete a book
    Book* deleteBookHelper(Book* node, int id) {
        if (!node) return nullptr;

        if (id < node->id) {
            node->left = deleteBookHelper(node->left, id);
        } else if (id > node->id) {
            node->right = deleteBookHelper(node->right, id);
        } else {
            if (!node->left) {
                Book* temp = node->right;
                delete node;
                return temp;
            } else if (!node->right) {
                Book* temp = node->left;
                delete node;
                return temp;
            }

            Book* temp = findMin(node->right);
            node->id = temp->id;
            node->title = temp->title;
            node->author = temp->author;
            node->year = temp->year;
            node->right = deleteBookHelper(node->right, temp->id);
        }
        return node;
    }

    // Helper function to find the minimum node
    Book* findMin(Book* node) {
        while (node && node->left) {
            node = node->left;
        }
        return node;
    }

public:
    Library() : root(nullptr) {}

    void addBook(int id, string title, string author, int year) {
        root = addBookHelper(root, id, title, author, year);
        cout << "Book added successfully!\n";
    }

    void searchBook(int id) {
        Book* book = searchBookHelper(root, id);
        if (book) {
            cout << "ID: " << book->id << ", Title: " << book->title
                 << ", Author: " << book->author << ", Year: " << book->year << endl;
        } else {
            cout << "Book not found!\n";
        }
    }

    void deleteBook(int id) {
        root = deleteBookHelper(root, id);
        cout << "Book deleted successfully!\n";
    }

    void displayBooks() {
        if (!root) {
            cout << "No books in the library.\n";
            return;
        }
        inOrderTraversal(root);
    }

    void saveToFile(const string& filename) {
        ofstream file(filename);
        if (!file.is_open()) {
            cout << "Error opening file for writing!\n";
            return;
        }

        stack<Book*> s;
        Book* current = root;
        while (current || !s.empty()) {
            while (current) {
                s.push(current);
                current = current->left;
            }
            current = s.top();
            s.pop();
            file << current->id << "," << current->title << "," << current->author << "," << current->year << "\n";
            current = current->right;
        }
        file.close();
        cout << "Library saved to file successfully!\n";
    }

    void loadFromFile(const string& filename) {
        ifstream file(filename);
        if (!file.is_open()) {
            cout << "Error opening file for reading!\n";
            return;
        }

        string line;
        while (getline(file, line)) {
            size_t pos = 0;
            vector<string> tokens;
            while ((pos = line.find(",")) != string::npos) {
                tokens.push_back(line.substr(0, pos));
                line.erase(0, pos + 1);
            }
            tokens.push_back(line);

            if (tokens.size() == 4) {
                addBook(stoi(tokens[0]), tokens[1], tokens[2], stoi(tokens[3]));
            }
        }
        file.close();
        cout << "Library loaded from file successfully!\n";
    }
};

int main() {
    Library library;
    int choice;

    do {
        cout << "\nLibrary Management System\n";
        cout << "1. Add Book\n";
        cout << "2. Search Book\n";
        cout << "3. Delete Book\n";
        cout << "4. Display Books\n";
        cout << "5. Save to File\n";
        cout << "6. Load from File\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int id, year;
                string title, author;
                cout << "Enter book ID: ";
                cin >> id;
                cin.ignore();
                cout << "Enter book title: ";
                getline(cin, title);
                cout << "Enter book author: ";
                getline(cin, author);
                cout << "Enter book year: ";
                cin >> year;
                library.addBook(id, title, author, year);
                break;
            }
            case 2: {
                int id;
                cout << "Enter book ID to search: ";
                cin >> id;
                library.searchBook(id);
                break;
            }
            case 3: {
                int id;
                cout << "Enter book ID to delete: ";
                cin >> id;
                library.deleteBook(id);
                break;
            }
            case 4:
                library.displayBooks();
                break;
            case 5: {
                string filename;
                cout << "Enter filename to save: ";
                cin >> filename;
                library.saveToFile(filename);
                break;
            }
            case 6: {
                string filename;
                cout << "Enter filename to load: ";
                cin >> filename;
                library.loadFromFile(filename);
                break;
            }
            case 0:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice!\n";
        }
    } while (choice != 0);

    return 0;
}